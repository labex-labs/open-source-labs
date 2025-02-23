# 関数をアンカリングする

指定された深さまで関数をアンカリングするには、`uncurry` 関数を使用します。

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

`uncurry` 関数を使用するには、アンカリングしたい関数と、アンカリングする深さを引数として渡します。この関数は、渡したい引数で呼び出せる可変長関数を返します。

深さを指定しない場合、関数は深さ `1` までアンカリングします。

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

渡す引数の数が指定された深さより少ない場合、関数は `RangeError` をスローします。
