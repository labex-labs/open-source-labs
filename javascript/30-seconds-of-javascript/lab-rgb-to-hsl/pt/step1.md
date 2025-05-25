# Conversão de RGB para HSL

Para converter um tuplo de cores RGB para o formato HSL, siga estes passos:

1.  Abra o Terminal/SSH para começar a praticar a codificação.
2.  Digite `node` e pressione Enter.
3.  Use a [fórmula de conversão de RGB para HSL](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/) para converter para o formato apropriado.
4.  Certifique-se de que todos os parâmetros de entrada estejam dentro da faixa de \[0, 255].
5.  Os valores resultantes devem estar dentro da faixa de H: \[0, 360], S: \[0, 100], L: \[0, 100].

Aqui está um exemplo da função RGBToHSL em JavaScript:

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

Aqui está um exemplo de como usar a função RGBToHSL:

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
