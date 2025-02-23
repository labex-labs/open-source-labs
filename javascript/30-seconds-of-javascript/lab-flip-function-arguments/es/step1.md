# Reordenar los argumentos de una función con flip

Para intercambiar el orden de los argumentos de una función, utiliza la función `flip`. Esta función toma una función como argumento y devuelve una nueva función que intercambia el primer y el último argumento.

Para implementar `flip`:

- Utiliza la extracción de argumentos y una clausura con argumentos variádicos.
- Junta el primer argumento utilizando el operador de propagación (`...`) para que sea el último argumento antes de aplicar los demás.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

Este es un ejemplo de cómo utilizar `flip` para reordenar los argumentos de `Object.assign`:

```js
let a = { name: "John Smith" };
let b = {};

// Crea una nueva función que intercambia los argumentos de Object.assign
const mergeFrom = flip(Object.assign);

// Crea una nueva función que une el primer argumento a a
let mergePerson = mergeFrom.bind(null, a);

// Llama a la nueva función con b como segundo argumento
mergePerson(b); // b ahora es igual a a

// Alternativamente, combina a y b sin utilizar la nueva función
b = {};
Object.assign(b, a); // b ahora es igual a a
```
