# Así es como se ejecuta una función para cada elemento del array en orden inverso

Para ejecutar una función para cada elemento del array, comenzando desde el último elemento del array, siga estos pasos:

1. Clone el array dado utilizando `Array.prototype.slice()`.
2. Invierta el array clonado utilizando `Array.prototype.reverse()`.
3. Utilice `Array.prototype.forEach()` para iterar sobre el array invertido.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

Puede probar la función ejecutando el siguiente código:

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

Para comenzar a codificar, abra la Terminal/SSH y escriba `node`.
