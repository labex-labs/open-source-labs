# Como Obter um Array Sem o Último Elemento

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Veja como você pode retornar todos os elementos de um array, exceto o último:

- Use `Array.prototype.slice()` para retornar todos os elementos do array, exceto o último.

```js
const initial = (arr) => arr.slice(0, -1);
```

Aqui está um exemplo:

```js
initial([1, 2, 3]); // [1, 2]
```
