# Cómo congelar profundamente un objeto en JavaScript

Para congelar profundamente un objeto en JavaScript, siga estos pasos:

1. Utilice `Object.keys()` para obtener todas las propiedades del objeto pasado.
2. Itere sobre las propiedades utilizando `Array.prototype.forEach()`.
3. Llame recursivamente a `Object.freeze()` en todas las propiedades que son objetos, aplicando `deepFreeze()` si es necesario.
4. Finalmente, utilice `Object.freeze()` para congelar el objeto dado.

Aquí está el código:

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

Puede probar el objeto congelado profundamente utilizando el siguiente código:

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // no permitido
val[1][0] = 4; // tampoco está permitido
```

El código anterior generará un error porque el objeto `val` está congelado profundamente y no se puede modificar.
