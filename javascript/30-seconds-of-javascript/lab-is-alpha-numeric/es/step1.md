# Verificar si una cadena es alfanumérica

Si deseas practicar la codificación, abre la Terminal/SSH y escribe `node`. Aquí hay una función que verifica si una cadena contiene solo caracteres alfanuméricos:

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

Para usarla, llama a `isAlphaNumeric` con una cadena como argumento. Devolverá `true` si la cadena contiene solo caracteres alfanuméricos y `false` en caso contrario.

Por ejemplo:

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false (contiene un espacio)
isAlphaNumeric("#$hello"); // false (contiene caracteres no alfanuméricos)
```

El método `RegExp.prototype.test()` se utiliza para verificar si la cadena de entrada coincide con el patrón alfanumérico, que está representado por la expresión regular `/^[a-z0-9]+$/gi`. Este patrón coincide con cualquier secuencia de una o más letras minúsculas o dígitos, y las banderas `g` e `i` hacen que la coincidencia sea insensible a mayúsculas y minúsculas.
