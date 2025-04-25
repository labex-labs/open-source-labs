# 检查环境是否为 Travis CI

要检查你是否在 Travis CI 上运行，请使用 `isTravisCI()` 函数。此函数检查 `TRAVIS` 和 `CI` 环境变量是否存在。

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

要在 Travis CI 上开始编码，请打开终端/SSH 并输入 `node`。
