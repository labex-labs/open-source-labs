# Listen for an Event Only Once

> To start practicing coding, open the Terminal/SSH and type `node`.

Adds an event listener to an element that will only run the callback the first time the event is triggered.

- Use `EventTarget.addEventListener()` to add an event listener to an element.
- Use `{ once: true }` as options to only run the given callback once.

```js
const listenOnce = (el, evt, fn) =>
  el.addEventListener(evt, fn, { once: true });
```

```js
listenOnce(
  document.getElementById('my-id'),
  'click',
  () => console.log('Hello world')
); // 'Hello world' will only be logged on the first click
```
