# Cómo asignar valores predeterminados a las propiedades de un objeto

Para asignar valores predeterminados a todas las propiedades de un objeto que son `undefined`, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.assign()` para crear un nuevo objeto vacío y copie el original para mantener el orden de las claves.
3. Utilice `Array.prototype.reverse()` y el operador de propagación (`...`) para combinar los valores predeterminados de izquierda a derecha.
4. Finalmente, utilice `obj` nuevamente para sobrescribir las propiedades que originalmente tenían un valor.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

Este fragmento de código devolverá un objeto que tiene valores predeterminados para todas las propiedades que eran indefinidas en el objeto original.
