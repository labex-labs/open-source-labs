# 함수 언커리 (Uncurry)

지정된 깊이까지 함수를 언커리하려면 `uncurry` 함수를 사용합니다.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

`uncurry` 함수를 사용하려면 언커리하려는 함수와 언커리하려는 깊이를 인수로 전달합니다. 이 함수는 전달하려는 인수로 호출할 수 있는 가변 인자 함수를 반환합니다.

깊이를 지정하지 않으면 함수는 깊이 `1`까지 언커리됩니다.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

전달하는 인수의 수가 지정된 깊이보다 적으면 함수는 `RangeError`를 발생시킵니다.
