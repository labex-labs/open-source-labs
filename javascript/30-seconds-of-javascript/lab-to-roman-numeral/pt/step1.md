# Convertendo Inteiro para Numeral Romano

Para converter um inteiro em sua representação de numeral romano, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2.  A função `toRomanNumeral()` aceita valores entre `1` e `3999` (inclusive).

3.  Crie uma tabela de consulta (lookup table) contendo arrays de 2 valores na forma de (valor romano, inteiro).

4.  Use `Array.prototype.reduce()` para percorrer os valores em `lookup` e dividir repetidamente `num` pelo valor.

5.  Use `String.prototype.repeat()` para adicionar a representação do numeral romano ao acumulador.

Aqui está o código para a função `toRomanNumeral()`:

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

Você pode testar a função com estes exemplos:

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
