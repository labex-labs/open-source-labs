# Convertendo Array para Lista HTML

Para começar a codificar, inicie o Terminal/SSH e digite `node`.

Esta função converte os elementos do array fornecido em tags `<li>` e os adiciona à lista com o ID fornecido.

Use `Array.prototype.map()` e `Document.querySelector()` para gerar uma lista de tags HTML.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Exemplo de uso:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
