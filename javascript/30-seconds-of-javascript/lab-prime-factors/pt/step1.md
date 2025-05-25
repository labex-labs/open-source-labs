# Como Encontrar os Fatores Primos de um Número usando o Algoritmo da Divisão por Tentativa

Para encontrar os fatores primos de um determinado número usando o algoritmo da divisão por tentativa (trial division algorithm), siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use um loop `while` para iterar sobre todos os possíveis fatores primos, começando com `2`.
- Se o fator atual, `f`, dividir exatamente `n`, adicione `f` ao array de fatores e divida `n` por `f`. Caso contrário, incremente `f` em um.
- A função `primeFactors` recebe um número `n` como entrada e retorna um array de seus fatores primos.
- Para testar a função, chame `primeFactors(147)` e ela retornará `[3, 7, 7]`.

Aqui está o código JavaScript:

```js
const primeFactors = (n) => {
  let a = [],
    f = 2;
  while (n > 1) {
    if (n % f === 0) {
      a.push(f);
      n /= f;
    } else {
      f++;
    }
  }
  return a;
};
```

Lembre-se de substituir `147` pelo número do qual você deseja encontrar os fatores primos.
