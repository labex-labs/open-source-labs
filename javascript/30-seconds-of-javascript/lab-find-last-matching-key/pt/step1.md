# Função para Encontrar a Última Chave que Corresponde a uma Condição

Para encontrar a última chave em um objeto que satisfaz uma condição dada, use a função `findLastKey`. Esta função recebe um objeto e uma função de teste como argumentos. Se uma chave correspondente for encontrada, a função a retorna. Caso contrário, ela retorna `undefined`. Aqui estão as etapas que a função segue para encontrar a última chave:

1.  Use `Object.keys()` para obter todas as propriedades do objeto.
2.  Use `Array.prototype.reverse()` para inverter a ordem das chaves.
3.  Use `Array.prototype.find()` para testar a função fornecida para cada par chave-valor. A função de callback recebe três argumentos - o valor, a chave e o objeto.
4.  Se uma chave correspondente for encontrada, retorne-a.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

Aqui está um exemplo de como usar `findLastKey`:

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

Para usar esta função, abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
