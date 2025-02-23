# Función para comprobar si una cadena es una URL absoluta

Para comprobar si una cadena dada es una URL absoluta, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `RegExp.prototype.test()` para probar si la cadena es una URL absoluta.
3. La función debe definirse como `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4. La función toma un argumento de cadena `str` y devuelve `true` si la cadena es una URL absoluta, y `false` en caso contrario.
5. Pruebe la función utilizando los ejemplos proporcionados:

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
