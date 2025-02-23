# Función para comprobar si una cadena es alfabética

Para comprobar si una cadena contiene solo caracteres alfabéticos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `RegExp.prototype.test()` para comprobar si la cadena dada coincide con el patrón de expresión regular alfabética.
- La función `isAlpha` toma una cadena como argumento y devuelve `true` si la cadena contiene solo caracteres alfabéticos, y `false` en caso contrario.

Aquí hay un ejemplo:

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
