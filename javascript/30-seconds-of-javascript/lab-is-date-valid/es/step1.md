# Cómo comprobar si una fecha es válida

Para comprobar si una fecha es válida, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador de propagación (`...`) para pasar la matriz de argumentos al constructor `Date`.
3. Utilice `Date.prototype.valueOf()` y `Number.isNaN()` para comprobar si se puede crear un objeto `Date` válido a partir de los valores dados.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

Puede probar la función con diferentes valores, como se muestra a continuación:

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
