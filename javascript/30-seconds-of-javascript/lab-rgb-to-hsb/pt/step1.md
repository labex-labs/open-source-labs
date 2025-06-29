# Conversão de RGB para HSB

Para converter uma tupla de cores RGB para o formato HSB, você pode seguir estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a [fórmula de conversão de RGB para HSB](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) para converter a tupla de cores RGB para o formato HSB apropriado.
3.  Os parâmetros de entrada variam de \[0, 255], enquanto os valores resultantes têm uma variação de:
    - H: \[0, 360]
    - S: \[0, 100]
    - B: \[0, 100]

Aqui está a função em JavaScript:

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

Você pode chamar a função assim:

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
