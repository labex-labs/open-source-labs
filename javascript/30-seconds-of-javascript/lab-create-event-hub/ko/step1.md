# 이벤트 허브 생성

`emit`, `on`, 그리고 `off` 메서드를 가진 이벤트 허브를 생성하려면 다음 단계를 따르세요:

1. `Object.create(null)`을 사용하여 `Object.prototype`에서 속성을 상속받지 않는 빈 `hub` 객체를 생성합니다.
2. `emit`의 경우, `event` 인수를 기반으로 핸들러 배열을 찾은 다음, 데이터를 인수로 전달하여 `Array.prototype.forEach()`를 사용하여 각 핸들러를 실행합니다.
3. `on`의 경우, 이벤트가 아직 존재하지 않으면 해당 이벤트를 위한 배열을 생성한 다음, `Array.prototype.push()`를 사용하여 핸들러를 배열에 추가합니다.
4. `off`의 경우, `Array.prototype.findIndex()`를 사용하여 이벤트 배열에서 핸들러의 인덱스를 찾고, `Array.prototype.splice()`를 사용하여 제거합니다.

다음은 코드입니다:

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

이벤트 허브를 사용하려면:

1. `on()`을 사용하여 다양한 유형의 이벤트를 수신 대기하여 이벤트를 구독합니다.
2. `emit()`을 사용하여 구독된 모든 핸들러를 호출하기 위해 이벤트를 게시하고, 데이터를 인수로 전달합니다.
3. `off()`를 사용하여 특정 핸들러가 이벤트를 수신 대기하는 것을 중지하여 이벤트 구독을 취소합니다.

다음은 예시입니다:

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// Subscribe: listen for different types of events
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Publish: emit events to invoke all handlers subscribed to them, passing the data to them as an argument
hub.emit("message", "hello world"); // logs 'hello world' and 'Message event fired'
hub.emit("message", { hello: "world" }); // logs the object and 'Message event fired'
hub.emit("increment"); // `increment` variable is now 1

// Unsubscribe: stop a specific handler from listening to the 'message' event
hub.off("message", handler);
```
