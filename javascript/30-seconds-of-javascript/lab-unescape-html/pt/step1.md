# Unescape HTML (Desfazer Escape HTML)

Esta função "unescapa" caracteres HTML "escapados". Para usá-la, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node`.
3. Copie e cole o seguinte código:

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

4. Chame a função `unescapeHTML` e passe a ela uma string com caracteres "escapados".
5. A função retornará a string "unescapada".

Exemplo de uso:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
