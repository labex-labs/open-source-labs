# Cómo extraer valores de un array en JavaScript

Para extraer valores específicos de un array en JavaScript, puedes utilizar los métodos `Array.prototype.filter()` y `Array.prototype.includes()`. Aquí te muestra cómo hacerlo:

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

La función `pull` toma un array y uno o más argumentos que representan los valores que se deben eliminar. Luego, la función crea un nuevo array filtrando los valores especificados utilizando `Array.prototype.filter()`. A continuación, muta el array original reiniciando su longitud a `0` y repoblando solo con los valores extraídos utilizando `Array.prototype.push()`.

Aquí te muestra un ejemplo de cómo utilizar la función `pull`:

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

En este ejemplo, la función `pull` elimina todas las ocurrencias de `'a'` y `'c'` del array `myArray` y devuelve un nuevo array con solo los valores `'b'` y `'b'`.
