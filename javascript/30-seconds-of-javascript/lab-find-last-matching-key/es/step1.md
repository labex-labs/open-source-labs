# Función para Encontrar la Última Clave que Cumpla una Condición

Para encontrar la última clave en un objeto que satisface una condición dada, utiliza la función `findLastKey`. Esta función toma un objeto y una función de prueba como argumentos. Si se encuentra una clave que coincide, la función la devuelve. De lo contrario, devuelve `undefined`. Estos son los pasos que la función sigue para encontrar la última clave:

1. Utiliza `Object.keys()` para obtener todas las propiedades del objeto.
2. Utiliza `Array.prototype.reverse()` para invertir el orden de las claves.
3. Utiliza `Array.prototype.find()` para probar la función proporcionada para cada par clave-valor. La función de devolución de llamada recibe tres argumentos: el valor, la clave y el objeto.
4. Si se encuentra una clave que coincide, devuélvala.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

Este es un ejemplo de uso de `findLastKey`:

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

Para utilizar esta función, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
