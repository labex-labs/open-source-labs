# Función que agrega argumentos

Para crear una función que agregue argumentos a los que recibe, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar la práctica de codificación.
2. Utilice el operador de propagación (`...`) para agregar `partials` a la lista de argumentos de `fn`.
3. Utilice el siguiente código para crear la función:

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. Pruebe la función con un ejemplo, como:

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
