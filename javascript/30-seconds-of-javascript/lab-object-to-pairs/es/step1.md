# Convertir un objeto en una matriz de pares clave-valor

Para convertir un objeto en una matriz de pares clave-valor, puedes seguir estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Object.entries()` para obtener una matriz de matrices de pares clave-valor a partir del objeto.
3. Cree una función llamada `objectToPairs` que acepte un objeto como argumento y devuelva la matriz de pares clave-valor.
4. Llame a la función `objectToPairs` con un objeto de ejemplo para probar la salida.

A continuación, se muestra una implementación de ejemplo:

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

Siguiendo estos pasos, puedes convertir fácilmente un objeto en una matriz de pares clave-valor utilizando JavaScript.
