# Recuperar Ancestrais de Elementos

Para recuperar os ancestrais de um elemento, desde a raiz do documento até o elemento especificado, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Node.parentNode` e um loop `while` para subir na árvore de ancestrais do elemento.
3.  Use `Array.prototype.unshift()` para adicionar cada novo ancestral ao início do array.

Aqui está um código de exemplo que implementa os passos acima:

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

Para recuperar os ancestrais de um elemento específico, use o método `querySelector()` para selecionar o elemento e passe-o como um argumento para a função `getAncestors()`. Por exemplo:

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

Isso retornará um array de todos os ancestrais do elemento especificado, na ordem da raiz do documento até o próprio elemento.
