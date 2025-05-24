# Inicializando um Array 2D em JavaScript

Para inicializar um array 2D em JavaScript, você pode usar o seguinte código:

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

Este código usa `Array.from()` e `Array.prototype.map()` para criar um array de `height` linhas, onde cada linha é um novo array de comprimento `width`. Ele também usa `Array.prototype.fill()` para definir todos os itens no array para o parâmetro `value`. Se nenhum `value` for fornecido, ele assume o valor padrão de `null`.

Você pode chamar a função assim:

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

Isso criará um array 2D com largura de 2, altura de 2, e todos os valores definidos como 0.
