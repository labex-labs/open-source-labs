# Função para Limitar um Número dentro de um Intervalo

Para limitar um número dentro de um intervalo especificado, use a função `clampNumber`.

Para começar, abra o Terminal/SSH e digite `node` para praticar a codificação.

A função `clampNumber` recebe três parâmetros: `num`, `a` e `b`. Ela limita `num` dentro do intervalo inclusivo especificado pelos valores de limite `a` e `b` e retorna o resultado.

Se `num` estiver dentro do intervalo, a função retorna `num`. Caso contrário, ela retorna o número mais próximo no intervalo.

Aqui está o código para a função `clampNumber`:

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

E aqui estão alguns exemplos de como usar a função:

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
