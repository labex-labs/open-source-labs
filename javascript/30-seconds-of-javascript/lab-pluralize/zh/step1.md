# 使字符串变为复数形式

要根据给定数字使单词变为复数形式，请使用 `pluralize` 函数。首先打开终端/SSH 并输入 `node`。此函数可以根据输入数字返回单词的单数或复数形式。你还可以提供一个可选字典来使用自定义复数形式。

要定义 `pluralize` 函数，使用一个闭包，该闭包接受 `word` 和一个可选的 `plural` 形式。如果输入的 `num` 是 `-1` 或 `1`，则返回 `word` 的单数形式。否则，返回 `plural` 形式。如果未提供自定义 `plural` 形式，函数将使用默认的单数 `word` 加上 `s`。

如果第一个参数是一个对象，`pluralize` 函数将返回一个新函数，该函数可以使用提供的字典来解析 `word` 的正确复数形式。

以下是 `pluralize` 函数的实际应用：

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

你可以像这样使用 `pluralize` 函数：

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

如果你有一个自定义复数形式的字典，你可以创建一个 `autoPluralize` 函数，该函数会自动为给定的 `word` 使用正确的复数形式：

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
