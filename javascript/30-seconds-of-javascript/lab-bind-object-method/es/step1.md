# Función para enlazar un método de objeto

Para crear una función que enlace un método de objeto a su contexto y, opcionalmente, agregue parámetros adicionales al principio, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Defina una función que tome tres parámetros: el contexto del objeto, la clave del método y cualquier argumento adicional que se agregará al principio.
3. La función debe devolver una nueva función que use `Function.prototype.apply()` para enlazar el método al contexto del objeto.
4. Utilice el operador de propagación (`...`) para agregar cualquier parámetro adicional suministrado a los argumentos.
5. Aquí hay una implementación de ejemplo:

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. Para probar la función, cree un objeto con un método y enlícelo usando `bindKey()`. Luego, llame al método enlazado con algunos argumentos.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
