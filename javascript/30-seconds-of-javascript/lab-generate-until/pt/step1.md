# Gerando Valores Até que uma Condição Seja Atendida

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. Depois de fazer isso, você pode criar um _generator_ (gerador) que produz novos valores até que uma determinada condição seja atendida.

Para criar este _generator_, siga estes passos:

- Inicialize o `val` atual usando o valor `seed`.
- Use um loop `while` para continuar iterando enquanto a função `condition`, chamada com o `val` atual, retornar `false`.
- Use a palavra-chave `yield` para retornar o `val` atual e, opcionalmente, receber um novo valor _seed_, `nextSeed`.
- Use a função `next` para calcular o próximo valor a partir do `val` atual e do `nextSeed`.

Aqui está um exemplo de trecho de código:

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Você pode usar o _generator_ chamando-o com os argumentos apropriados. Por exemplo:

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

Isso produzirá um array de valores de `1` a `5`, pois a condição `v > 5` é atendida quando `val` é igual a `6`.
