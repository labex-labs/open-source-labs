# Creación del centro de eventos

Para crear un centro de eventos con los métodos `emit`, `on` y `off`, siga estos pasos:

1. Utilice `Object.create(null)` para crear un objeto `hub` vacío que no herede propiedades de `Object.prototype`.
2. Para `emit`, resuelva la matriz de manejadores basada en el argumento `event` y luego ejecute cada uno con `Array.prototype.forEach()` pasando los datos como argumento.
3. Para `on`, cree una matriz para el evento si aún no existe, luego use `Array.prototype.push()` para agregar el manejador a la matriz.
4. Para `off`, use `Array.prototype.findIndex()` para encontrar el índice del manejador en la matriz de eventos y eliminarlo usando `Array.prototype.splice()`.

Aquí está el código:

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

Para usar el centro de eventos:

1. Suscríbase a eventos escuchando diferentes tipos de eventos usando `on()`.
2. Publique eventos para invocar todos los manejadores suscritos a ellos, pasando los datos a ellos como argumento usando `emit()`.
3. Anule la suscripción a un evento deteniendo un manejador específico de escuchar el evento usando `off()`.

Aquí está un ejemplo:

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// Suscribirse: escuchar diferentes tipos de eventos
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Publicar: emitir eventos para invocar todos los manejadores suscritos a ellos, pasando los datos a ellos como argumento
hub.emit("message", "hello world"); // registra 'hello world' y 'Message event fired'
hub.emit("message", { hello: "world" }); // registra el objeto y 'Message event fired'
hub.emit("increment"); // la variable `increment` ahora es 1

// Anular la suscripción: detener un manejador específico de escuchar el evento 'message'
hub.off("message", handler);
```
