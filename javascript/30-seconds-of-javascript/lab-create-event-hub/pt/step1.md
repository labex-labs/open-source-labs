# Criação do Hub de Eventos

Para criar um hub de eventos com os métodos `emit`, `on` e `off`, siga os passos:

1.  Use `Object.create(null)` para criar um objeto `hub` vazio que não herda propriedades de `Object.prototype`.
2.  Para `emit`, resolva o array de handlers (manipuladores) com base no argumento `event` e, em seguida, execute cada um com `Array.prototype.forEach()`, passando os dados como um argumento.
3.  Para `on`, crie um array para o evento se ele ainda não existir, então use `Array.prototype.push()` para adicionar o handler ao array.
4.  Para `off`, use `Array.prototype.findIndex()` para encontrar o índice do handler no array de eventos e remova-o usando `Array.prototype.splice()`.

Aqui está o código:

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

Para usar o hub de eventos:

1.  Inscreva-se em eventos ouvindo diferentes tipos de eventos usando `on()`.
2.  Publique eventos para invocar todos os handlers inscritos neles, passando os dados para eles como um argumento usando `emit()`.
3.  Cancele a inscrição de um evento, impedindo que um handler específico ouça o evento usando `off()`.

Aqui está um exemplo:

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
