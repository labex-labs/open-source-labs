# Deshacer la escapación de HTML

Esta función deshace la escapación de los caracteres HTML escapados. Para utilizarla, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node`.
3. Copie y pegue el siguiente código:

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. Llame a la función `unescapeHTML` y pasele una cadena con caracteres escapados.
5. La función devolverá la cadena sin escapación.

Uso de ejemplo:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
