# Cómo crear una máscara para un valor en JavaScript

Para crear una máscara para un valor en JavaScript, puedes utilizar la función `mask()`. Sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `String.prototype.slice()` para obtener la porción de los caracteres que permanecerán sin máscara.
3. Utiliza `String.prototype.padStart()` para llenar el comienzo de la cadena con el carácter de `máscara` hasta la longitud original.
4. Si quieres excluir caracteres del final de la cadena, utiliza un valor negativo para `num`.
5. Si no especificas un valor para `num`, la función utilizará como valor predeterminado mantener los últimos 4 caracteres sin máscara.
6. Si no especificas un valor para `mask`, la función utilizará como valor predeterminado el carácter `'*'` para la máscara.

Aquí está el código para la función `mask()`:

```js
const mask = (cc, num = 4, mask = "*") =>
  `${cc}`.slice(-num).padStart(`${cc}`.length, mask);
```

Y aquí hay algunos ejemplos de cómo utilizar la función `mask()`:

```js
mask(1234567890); // '******7890'
mask(1234567890, 3); // '*******890'
mask(1234567890, -4, "$"); // '$$$$567890'
```
