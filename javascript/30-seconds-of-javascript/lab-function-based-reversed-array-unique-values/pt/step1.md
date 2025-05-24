# Função para Encontrar Valores Únicos Invertidos em Array

Para encontrar todos os valores únicos de um array com base em uma função comparadora fornecida, da direita para a esquerda, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduceRight()` e `Array.prototype.some()` para criar um array contendo apenas a última ocorrência única de cada valor, com base na função comparadora `fn`.
3.  A função comparadora recebe dois argumentos: os valores dos dois elementos que estão sendo comparados.
4.  Aqui está o código para implementar a função:

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5.  Use o seguinte código para testar a função:

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
