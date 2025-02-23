# Función promisify

Para convertir una función asincrónica para que devuelva una promesa, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la currying para devolver una función que devuelva una `Promise` que llama a la función original.
3. Utilice el operador rest (`...`) para pasar todos los parámetros.
4. Si está utilizando Node 8+ puede utilizar [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original).
5. Aquí hay un fragmento de código de ejemplo:

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. Para utilizar esta función, defina la función asincrónica y pásela como parámetro a la función `promisify`. La función devuelta ahora devolverá una promesa.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // La promesa se resuelve después de 2s
```

La función `delay` es un ejemplo de una función asincrónica que ahora devuelve una promesa utilizando la función `promisify`.
