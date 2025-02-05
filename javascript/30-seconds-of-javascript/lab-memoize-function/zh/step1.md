# 记忆化函数

要开始编码，请打开终端/SSH 并输入 `node`。此函数返回记忆化（缓存）函数。以下是使用此函数的步骤：

1. 实例化一个新的 `Map` 对象以创建一个空缓存。
2. 返回一个接受单个参数的函数，该参数将提供给记忆化函数。在执行函数之前，检查该特定输入值的输出是否已被缓存。如果是，则返回缓存的输出；否则，存储并返回它。
3. 使用 `function` 关键字，以便在必要时允许记忆化函数的 `this` 上下文发生变化。
4. 将 `cache` 设置为返回函数的一个属性，以便可以访问它。

以下是实现记忆化函数的代码：

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

要了解此函数的工作原理，可以将其与 `anagrams` 函数一起使用。以下是一个示例：

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // 耗时较长
anagramsCached("javascript"); // 由于已缓存，几乎立即返回
console.log(anagramsCached.cache); // 缓存的变位词映射
```
