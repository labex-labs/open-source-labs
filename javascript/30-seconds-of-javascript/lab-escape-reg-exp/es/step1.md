# Cómo escapar expresiones regulares en JavaScript

Para escapar una cadena para usarla en una expresión regular en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `String.prototype.replace()` para escapar los caracteres especiales.
3. Copia y pega el siguiente fragmento de código:

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. Utiliza la función `escapeRegExp()` para escapar los caracteres especiales en una cadena.

Aquí hay un ejemplo:

```js
escapeRegExp("(test)"); // \\(test\\)
```

Con estos pasos, ahora puedes escapar fácilmente cualquier carácter especial en una expresión regular en JavaScript.
