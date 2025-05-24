# Gerador que Produz Valores Enquanto uma Condição for Verdadeira

Para começar a codificar, abra o Terminal/SSH e digite `node`. Isso criará um gerador que continua produzindo novos valores enquanto a condição fornecida for atendida.

O gerador é inicializado com um valor inicial (`seed`), que é usado para inicializar o `val` atual. Um loop `while` é então usado para iterar enquanto a função `condition`, chamada com o `val` atual, retorna `true`.

A palavra-chave `yield` é usada para retornar o `val` atual e, opcionalmente, receber um novo valor inicial, `nextSeed`. A função `next` é usada para calcular o próximo valor a partir do `val` atual e do `nextSeed`.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Para usar o gerador, chame-o com as funções `seed`, `condition` e `next`. Por exemplo, chamar `[...generateWhile(1, v => v <= 5, v => ++v)]` retornará `[1, 2, 3, 4, 5]`.
