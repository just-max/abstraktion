# `abstraktion`
Multiline lambda expressions for Python.

## Usage

Don't.

## Example

```python
from abstraktion import *

print(*map(
  lambda upper: (
    import_(lambda random, /, randint: in_(
    let(lambda x = randint(0, 10): in_(
    let(lambda y = randint(~x, upper): in_(
    print(f"x={~x}"),
    print(f"y={~y}"),
    let(lambda sum = 0: in_(
    for_(lambda i, n = enumerate(range(~x, ~y)): in_(
      print(f"i={~i} n={~n} sum={~sum}"),
      if_(~i + ~n > 10).then(lambda: in_(
        n <= ~i - ~n,
      )).else_(lambda: in_(
        print("no change"),
      )),
      sum <= ~sum + ~n,
    )),
    sum,
  ))))))))),
  [30, 40, 50]
))
```

## Code Style

```shell
pip install black
black --line-length 69 abstraktion/
```

## License

Unlicense.

## Acknowledgements

Many thanks to Rainbow Brackets for sponsoring the development of this library.
