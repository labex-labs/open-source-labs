# Converter HSL para RGB usando JavaScript

Para converter uma tupla de cores no formato HSL para RGB, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a [fórmula de conversão de HSL para RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB) para converter a tupla de cores para o formato apropriado.
3.  Certifique-se de que os parâmetros de entrada estejam dentro das seguintes faixas: H: \[0, 360], S: \[0, 100], L: \[0, 100].
4.  Os valores de saída devem estar dentro da faixa \[0, 255].

Aqui está o código JavaScript para a fórmula de conversão de HSL para RGB:

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

Para usar a função, forneça os valores H, S e L como argumentos:

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
