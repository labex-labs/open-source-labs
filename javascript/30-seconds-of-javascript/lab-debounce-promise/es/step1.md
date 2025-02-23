# Promesa anti-rebote

Para crear una función anti-rebote que devuelva una promesa, retrasando la invocación de la función proporcionada hasta que hayan transcurrido al menos `ms` milisegundos desde la última vez que se invocó, siga los siguientes pasos:

1. Cada vez que se invoque la función anti-rebote, quite el temporizador pendiente actual con `clearTimeout()`, luego use `setTimeout()` para crear un nuevo temporizador que retrasará la invocación de la función hasta que hayan transcurrido al menos `ms` milisegundos.
2. Use `Function.prototype.apply()` para aplicar el contexto `this` a la función y proporcionar los argumentos necesarios.
3. Cree una nueva `Promise` y agregue sus devoluciones de llamada `resolve` y `reject` a la pila de promesas pendientes.
4. Cuando se llame a `setTimeout()`, copie la pila actual (ya que puede cambiar entre la llamada a la función proporcionada y su resolución), límpiela y llame a la función proporcionada.
5. Cuando la función proporcionada se resuelva/rechace, resuelva/rechace todas las promesas en la pila (copiada cuando se llamó a la función) con los datos devueltos.
6. Omita el segundo argumento, `ms`, para establecer el temporizador con un valor predeterminado de `0` ms.

A continuación, se muestra el código de la función `debouncePromise()`:

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

A continuación, se muestra un ejemplo de cómo usar `debouncePromise()`:

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Ambos veces mostrará ['resolved', 'bar']
```
