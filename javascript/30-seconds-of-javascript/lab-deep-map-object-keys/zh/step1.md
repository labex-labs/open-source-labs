# 深度映射对象键

要深度映射对象的键，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 将 `deepMapKeys` 函数与提供的对象以及一个生成新键的函数一起使用。
3. 该函数创建一个与提供的对象具有相同值的对象，其键是通过对每个键运行提供的函数生成的。
4. 使用 `Object.keys()` 遍历对象的键。
5. 使用 `Array.prototype.reduce()` 和提供的函数创建一个具有相同值和映射键的新对象。
6. 如果值是一个对象，则对其递归调用 `deepMapKeys` 以映射其键。

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

以下是 `deepMapKeys` 的一个示例用法：

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
