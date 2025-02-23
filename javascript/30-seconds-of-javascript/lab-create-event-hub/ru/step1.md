# Создание центра событий

Чтобы создать центр событий с методами `emit`, `on` и `off`, следуйте шагам:

1. Используйте `Object.create(null)` для создания пустого объекта `hub`, который не наследует свойства от `Object.prototype`.
2. Для `emit` определите массив обработчиков на основе аргумента `event`, а затем запустите каждый из них с использованием `Array.prototype.forEach()`, передав в него данные в качестве аргумента.
3. Для `on` создайте массив для события, если он еще не существует, а затем используйте `Array.prototype.push()`, чтобы добавить обработчик в массив.
4. Для `off` используйте `Array.prototype.findIndex()`, чтобы найти индекс обработчика в массиве событий, а затем удалите его с использованием `Array.prototype.splice()`.

Вот код:

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

Для использования центра событий:

1. Подписывайтесь на события, слушая разные типы событий с использованием `on()`.
2. Публикуйте события, чтобы вызвать все подписанные на них обработчики, передав в них данные в качестве аргумента с использованием `emit()`.
3. Отписывайтесь от события, остановив конкретный обработчик от прослушивания события с использованием `off()`.

Вот пример:

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// Подписка: слушать разные типы событий
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Публикация: эмиттировать события, чтобы вызвать все подписанные на них обработчики, передав в них данные в качестве аргумента
hub.emit("message", "hello world"); // выводит 'hello world' и 'Message event fired'
hub.emit("message", { hello: "world" }); // выводит объект и 'Message event fired'
hub.emit("increment"); // переменная `increment` теперь равна 1

// Отписка: остановить конкретный обработчик от прослушивания события 'message'
hub.off("message", handler);
```
