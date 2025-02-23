# Consejos para Codificar y Encontrar Claves Comunes

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para encontrar las claves comunes entre dos objetos, sigue estos pasos:

1. Utiliza `Object.keys()` para obtener las claves del primer objeto.
2. Utiliza `Object.prototype.hasOwnProperty()` para comprobar si el segundo objeto tiene una clave que está en el primer objeto.
3. Utiliza `Array.prototype.filter()` para filtrar las claves que no están en ambos objetos.

Aquí hay un ejemplo del código:

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

Puedes probar el código con este ejemplo:

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
