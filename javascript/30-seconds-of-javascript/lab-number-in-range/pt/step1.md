# Função para Verificar se um Número Está Dentro de um Intervalo Específico

Para verificar se um número se enquadra em um intervalo especificado, use a função `inRange`. Comece abrindo o Terminal/SSH e digitando `node` para começar a codificar.

Aqui estão os passos para usar a função `inRange`:

1.  Use a comparação aritmética para verificar se o número fornecido está no intervalo especificado.
2.  Se o segundo argumento, `end`, não for especificado, o intervalo é considerado de `0` a `start`.
3.  A função `inRange` recebe três argumentos: `n`, `start` e `end`.
4.  Se `end` for menor que `start`, a função troca os valores de `start` e `end`.
5.  Se `end` não for especificado, a função verifica se `n` é maior ou igual a 0 e menor que `start`.
6.  Se `end` for especificado, a função verifica se `n` é maior ou igual a `start` e menor que `end`.
7.  A função retorna `true` se `n` estiver dentro do intervalo especificado e `false` caso contrário.

Aqui está a função `inRange`:

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

Aqui estão alguns exemplos de como usar a função `inRange`:

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
