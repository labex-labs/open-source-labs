# Testando se Algum Elemento de um Array é _Truthy_

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Para verificar se algum elemento em uma coleção retorna `true` com base em uma função fornecida, use `Array.prototype.some()`. Se você quiser usar a função `Boolean` como padrão, pode omitir o segundo argumento, `fn`.

Aqui está um exemplo de código:

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

Você pode testá-lo usando os seguintes exemplos:

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
