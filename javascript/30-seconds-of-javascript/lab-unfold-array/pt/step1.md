# Unfold Array (Desdobrar Array)

Para criar um array usando uma função iteradora e um valor inicial (seed), siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use um loop `while` e `Array.prototype.push()` para chamar a função iteradora repetidamente até que ela retorne `false`.
3.  A função iteradora deve aceitar um argumento (`seed`) e sempre retornar um array com dois elementos ([`value`, `nextSeed`]) ou `false` para terminar.

Use o seguinte código para implementar a função `unfold`:

```js
const unfold = (fn, seed) => {
  let result = [],
    val = [null, seed];
  while ((val = fn(val[1]))) result.push(val[0]);
  return result;
};
```

Aqui está um exemplo de como usar a função `unfold`:

```js
var f = (n) => (n > 50 ? false : [-n, n + 10]);
unfold(f, 10); // [-10, -20, -30, -40, -50]
```

Isso produzirá um array com valores gerados pela função iteradora `f` começando do valor inicial (seed) de `10`. A função iteradora gera um array com dois elementos em cada passo: a negação do valor atual do seed e o próximo valor do seed, que é incrementado em 10. O processo continua até que o valor do seed seja maior que 50, momento em que a função retorna `false`.
