# Função Unwind de Objeto

Para "unwind" (desmembrar) um objeto por sua propriedade com valor de array, use a função `unwind`.

- Para começar a codificar, abra o Terminal/SSH e digite `node`.
- A função usa a desestruturação de objetos para excluir o par chave-valor para a `key` especificada do objeto.
- Em seguida, ela usa `Array.prototype.map()` para os valores da `key` fornecida para criar um array de objetos.
- Cada objeto contém os valores do objeto original, exceto para a `key`, que é mapeada para seus valores individuais.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

Exemplo de uso:

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
