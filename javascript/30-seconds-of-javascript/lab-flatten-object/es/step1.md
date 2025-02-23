# Aplanando un objeto

Para aplanar un objeto con rutas para las claves, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la recursividad para aplanar el objeto.
3. Utilice `Object.keys()` combinado con `Array.prototype.reduce()` para convertir cada nodo hoja en un nodo de ruta aplanada.
4. Si el valor de una clave es un objeto, llame a la función recursivamente con el `prefix` adecuado para crear la ruta utilizando `Object.assign()`.
5. De lo contrario, agregue el par clave-valor prefiijado adecuado al objeto acumulador.
6. Omita el segundo argumento, `prefix`, a menos que desee que cada clave tenga un prefijo.

A continuación, se muestra una implementación de ejemplo:

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

Puede usar la función `flattenObject` de la siguiente manera:

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
