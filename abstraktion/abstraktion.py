import importlib
import inspect
from inspect import Parameter


def import_(body):
    sig = iter(inspect.signature(body).parameters.values())
    module = importlib.import_module(next(sig).name)
    imports = (getattr(module, p.name) for p in sig)
    return body(module, *imports)


class var:
    UNDEFINED = object()

    def __init__(self, name, value=UNDEFINED):
        self.value = value
        self.name = name

    def __le__(self, value):
        self.value = value

    def __invert__(self):
        if self.value is var.UNDEFINED:
            raise ValueError(f"undefined variable '{name}'")
        return self.value


def let(body):
    kwargs = {
        name: var(
            name,
            var.UNDEFINED
            if p.default is Parameter.empty
            else p.default,
        )
        for name, p in inspect.signature(body).parameters.items()
    }
    return body(**kwargs)


def in_(*args):
    result = args[-1]
    return ~result if isinstance(result, var) else result


def for_(body):
    sig = list(inspect.signature(body).parameters.values())
    it = sig[-1].default
    for vs in it:
        body(*(var(sig[i].name, v) for i, v in enumerate(vs)))


class if_:
    def __init__(self, cond):
        self.cond = cond

    def then(self, body):
        if self.cond:
            body()
        return self

    def else_(self, body):
        if not self.cond:
            body()
        return self
