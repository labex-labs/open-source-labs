# Instruções para Extrair Valores de um Array de Objetos

Para extrair valores de um array de objetos, você pode seguir estas etapas:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.map()` para mapear o array de objetos para o valor de uma `key` especificada para cada objeto.
3. Implemente a seguinte função:

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. Teste a função com um array de objetos de exemplo:

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

Isso retornará um array de valores correspondentes à `key` especificada do array de objetos.
