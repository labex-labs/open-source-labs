# Algoritmo para barajar arrays

Para barajar un array en JavaScript, utiliza el algoritmo de Fisher-Yates. Este algoritmo reordena los elementos del array de forma aleatoria y devuelve un nuevo array.

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí está el código para el algoritmo de Fisher-Yates:

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

Para barajar un array, pasa el array a la función `shuffle` y devolverá el array barajado. Por ejemplo:

```js
const foo = [1, 2, 3];
shuffle(foo); // devuelve [2, 3, 1], y foo sigue siendo [1, 2, 3]
```
