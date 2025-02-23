# Función para Desenrollar Objeto

Para desenrollar un objeto por su propiedad con valores de matriz, use la función `unwind`.

- Para comenzar a codificar, abra la Terminal/SSH y escriba `node`.
- La función utiliza la extracción de objetos para excluir el par clave-valor para la `key` especificada del objeto.
- Luego, utiliza `Array.prototype.map()` para los valores de la `key` dada para crear una matriz de objetos.
- Cada objeto contiene los valores del objeto original, excepto `key` que se mapea a sus valores individuales.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

Uso de ejemplo:

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
