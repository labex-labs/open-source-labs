# Cómo truncar una cadena en blanco en JavaScript

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función que trunca una cadena hasta una longitud especificada respetando el espacio en blanco siempre que sea posible:

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

Para usar esta función, pasa la cadena que quieres truncar como primer argumento, la longitud máxima como segundo argumento y una cadena de terminación opcional como tercer argumento. Si la longitud de la cadena es menor o igual que el límite especificado, se devolverá la cadena original. De lo contrario, la función buscará el último espacio antes del límite y truncará la cadena en ese punto, agregando la cadena de terminación si se especifica.

Aquí hay algunos ejemplos:

```js
truncateStringAtWhitespace("short", 10); //'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
