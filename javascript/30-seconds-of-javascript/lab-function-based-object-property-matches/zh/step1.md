# 使用函数匹配对象属性

要开始练习编码，请打开终端/SSH 并输入 `node`。

此函数用于比较两个对象，并检查第一个对象是否包含与第二个对象等效的属性值。它会根据提供的函数来进行此操作。

要使用此函数，请遵循以下步骤：

- 使用 `Object.keys()` 获取第二个对象的所有键。
- 使用 `Array.prototype.every()`、`Object.prototype.hasOwnProperty()` 和提供的函数来确定第一个对象中是否存在所有键并且具有等效值。
- 如果未提供函数，则使用相等运算符比较值。

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

以下是如何使用此函数的示例：

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

此示例检查两个对象在 `greeting` 属性上是否具有等效值。它使用 `isGreeting` 函数来确保两个值都是有效的问候语。
