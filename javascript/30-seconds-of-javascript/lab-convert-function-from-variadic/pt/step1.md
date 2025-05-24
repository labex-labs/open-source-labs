# Convertendo uma Função Variádica

Para converter uma função variádica, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a codificar.
2. Crie uma função que recebe uma função variádica.
3. Use uma closure e o operador spread (`...`) para mapear o array de argumentos para as entradas da função.
4. Retorne uma nova função que aceita um array de argumentos e chama a função variádica original com esses argumentos.

Aqui está um exemplo de como usar esta técnica para converter a função `Math.max`:

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
