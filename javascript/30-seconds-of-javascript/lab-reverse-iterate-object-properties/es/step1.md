# Así es como iterar sobre las propiedades propias de un objeto en orden inverso

Para iterar sobre las propiedades propias de un objeto en orden inverso y ejecutar una devolución de llamada para cada una, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` para obtener todas las propiedades del objeto.
3. Utilice `Array.prototype.reverse()` para invertir el orden de las propiedades.
4. Utilice `Array.prototype.forEach()` para ejecutar la función proporcionada para cada par clave-valor.
5. La función de devolución de llamada debe tener tres argumentos: el valor, la clave y el objeto.

Aquí está el código:

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

Puede utilizar esta función con cualquier objeto y función de devolución de llamada. Por ejemplo, para registrar los valores de `{ foo: 'bar', a: 1 }` en orden inverso, puede utilizar el siguiente código:

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
