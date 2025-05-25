# Como arredondar um número para uma precisão específica em JavaScript:

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- Use `Math.round()` e _template literals_ para arredondar o número para o número especificado de dígitos.
- Se você deseja arredondar para um inteiro, omita o segundo argumento, `decimals`.
- Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
- Por exemplo, `round(1.005, 2)` retornará `1.01`.
