# Event-Hub-Erstellung

Um einen Event-Hub mit den Methoden `emit`, `on` und `off` zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie `Object.create(null)`, um ein leeres `hub`-Objekt zu erstellen, das keine Eigenschaften von `Object.prototype` erbt.
2. Für `emit` lösen Sie das Array von Handlern basierend auf dem `event`-Argument auf und führen Sie jedes Element mit `Array.prototype.forEach()` aus, indem Sie die Daten als Argument übergeben.
3. Für `on` erstellen Sie ein Array für das Ereignis, wenn es noch nicht existiert, und verwenden Sie dann `Array.prototype.push()`, um den Handler zum Array hinzuzufügen.
4. Für `off` verwenden Sie `Array.prototype.findIndex()`, um den Index des Handlers im Ereignisarray zu finden und es mit `Array.prototype.splice()` zu entfernen.

Hier ist der Code:

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

Um den Event-Hub zu verwenden:

1. Abonnieren Sie Ereignisse, indem Sie mit `on()` auf verschiedene Ereignistypen lauschen.
2. Verteilen Sie Ereignisse, um alle abonnierten Handler aufzurufen, und übergeben Sie die Daten als Argument an sie mit `emit()`.
3. Abmelden Sie sich von einem Ereignis, indem Sie einen bestimmten Handler davon abhalten, auf das Ereignis zu lauschen, mit `off()`.

Hier ist ein Beispiel:

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// Abonnieren: Lauschen Sie auf verschiedene Ereignistypen
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Verteilen: Emitieren Sie Ereignisse, um alle abonnierten Handler aufzurufen, und übergeben Sie die Daten als Argument an sie
hub.emit("message", "hello world"); // gibt 'hello world' und 'Message event fired' aus
hub.emit("message", { hello: "world" }); // gibt das Objekt und 'Message event fired' aus
hub.emit("increment"); // Die Variable `increment` hat jetzt den Wert 1

// Abmelden: Stoppen Sie einen bestimmten Handler davon, auf das 'message'-Ereignis zu lauschen
hub.off("message", handler);
```
