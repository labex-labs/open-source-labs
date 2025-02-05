# 获取基础URL

要从给定的URL中获取基础URL，请按以下步骤操作：

1. 打开终端/SSH。
2. 输入 `node` 开始练习编码。
3. 使用以下JavaScript函数获取当前URL，不包含任何参数或片段标识符：

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. 将 `url` 替换为你要从中获取基础URL的URL。
5. 如果找到 `'?'` 或 `'#'`，该函数将删除其后的所有内容，并返回基础URL。
6. 以下是一个示例：

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
