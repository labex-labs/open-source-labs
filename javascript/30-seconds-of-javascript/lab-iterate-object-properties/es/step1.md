# Cómo iterar sobre las propiedades propias de un objeto en JavaScript

Para iterar sobre las propiedades propias de un objeto y practicar la codificación, siga estos pasos:

1. Abra la Terminal o SSH.
2. Escriba `node` para iniciar una nueva sesión de Node.js.
3. Utilice el método `Object.keys()` para recuperar una matriz de las propiedades propias del objeto.
4. Utilice el método `Array.prototype.forEach()` para recorrer cada propiedad y ejecutar una función proporcionada.
5. La función proporcionada debe aceptar tres argumentos: el valor de la propiedad, la clave de la propiedad y el objeto en sí.
6. Utilice la función `forOwn()` con el objeto y la función proporcionada para iterar sobre las propiedades del objeto.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

Este código registrará los valores de las propiedades `foo` y `a` en la consola.
