# Compreendendo a Aridade de Função Unária

Para começar a codificar, abra o Terminal/SSH e digite `node`.

A aridade de função unária (unary function arity) refere-se a uma função que aceita apenas um argumento, ignorando quaisquer argumentos adicionais.

A função fornecida `fn` pode ser chamada com apenas o primeiro argumento fornecido. Para criar uma função unária, use o seguinte código:

```js
const unary = (fn) => (val) => fn(val);
```

Um exemplo de uso de `unary` com a função `parseInt` é mostrado abaixo:

```js
["6", "8", "10"].map(unary(parseInt)); // [6, 8, 10]
```
