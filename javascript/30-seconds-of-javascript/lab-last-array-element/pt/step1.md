# Como Obter o Último Elemento de um Array em JavaScript

Para começar a codificar, abra o Terminal/SSH e digite `node`. A seguinte função retorna o último elemento em um array:

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

Para usá-la, você precisa fornecer um array como argumento. A função verifica se o array é _truthy_ (avaliado como verdadeiro) e possui uma propriedade `length`. Se ambas as condições forem verdadeiras, ela calcula o índice do último elemento do array e o retorna. Caso contrário, retorna `undefined`.

Aqui estão alguns exemplos:

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
