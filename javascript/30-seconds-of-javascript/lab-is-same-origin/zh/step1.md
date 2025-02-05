# 检查两个URL是否同源

要检查两个URL是否同源：

1. 打开终端/SSH并输入 `node` 以开始练习编码。

2. 使用 `URL.protocol` 和 `URL.host` 检查两个URL是否具有相同的协议和主机。

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. 使用你要比较的URL创建两个URL对象。

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. 将两个URL对象作为参数调用 `isSameOrigin` 函数以获得布尔输出。

```js
isSameOrigin(origin, destination); // true
```

5. 你也可以使用其他URL测试该函数，以查看它们是否同源。

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
