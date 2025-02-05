# 创建事件中心

要创建一个具有 `emit`、`on` 和 `off` 方法的事件中心，请按以下步骤操作：

1. 使用 `Object.create(null)` 创建一个空的 `hub` 对象，该对象不会从 `Object.prototype` 继承属性。
2. 对于 `emit`，根据 `event` 参数解析处理程序数组，然后通过将数据作为参数传入，使用 `Array.prototype.forEach()` 运行每个处理程序。
3. 对于 `on`，如果事件的数组尚不存在，则为该事件创建一个数组，然后使用 `Array.prototype.push()` 将处理程序添加到数组中。
4. 对于 `off`，使用 `Array.prototype.findIndex()` 在事件数组中找到处理程序的索引，并使用 `Array.prototype.splice()` 将其删除。

以下是代码：

```js
const createEventHub = () => ({
  hub: Object.create(null),
  emit(event, data) {
    (this.hub[event] || []).forEach((handler) => handler(data));
  },
  on(event, handler) {
    if (!this.hub[event]) this.hub[event] = [];
    this.hub[event].push(handler);
  },
  off(event, handler) {
    const i = (this.hub[event] || []).findIndex((h) => h === handler);
    if (i > -1) this.hub[event].splice(i, 1);
    if (this.hub[event].length === 0) delete this.hub[event];
  }
});
```

要使用事件中心：

1. 通过使用 `on()` 监听不同类型的事件来订阅事件。
2. 发布事件以调用所有订阅它们的处理程序，并使用 `emit()` 将数据作为参数传递给它们。
3. 通过使用 `off()` 阻止特定处理程序监听事件来取消订阅事件。

以下是一个示例：

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// 订阅：监听不同类型的事件
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// 发布：发布事件以调用所有订阅它们的处理程序，并将数据作为参数传递给它们
hub.emit("message", "hello world"); // 输出 'hello world' 和 'Message event fired'
hub.emit("message", { hello: "world" }); // 输出对象和 'Message event fired'
hub.emit("increment"); // `increment` 变量现在为 1

// 取消订阅：阻止特定处理程序监听'message' 事件
hub.off("message", handler);
```
