# Búsqueda de subcadena sin distinción de mayúsculas y minúsculas

Para comprobar si una cadena contiene una subcadena independientemente de la capitalización, siga estos pasos:

- Utilice el constructor `RegExp` con la bandera `'i'` para crear una expresión regular que coincida con la `searchString` dada, ignorando la capitalización.
- Utilice `RegExp.prototype.test()` para comprobar si la cadena contiene la subcadena.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

Para probar esta función, puede ejecutar:

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
