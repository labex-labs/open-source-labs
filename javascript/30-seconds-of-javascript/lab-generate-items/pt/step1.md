# Prática de Código

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. Em seguida, você pode usar a função `generateItems` para gerar um array com um número específico de itens.

- Chame `generateItems` com o número desejado de itens e uma função que será usada para gerar os itens.
- `generateItems` usa `Array.from()` para criar um array vazio do comprimento especificado e chama a função fornecida com o índice de cada elemento recém-criado.
- A função fornecida recebe um argumento - o índice de cada elemento.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

Aqui está um exemplo de como usar `generateItems` para gerar um array de 10 números aleatórios:

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
