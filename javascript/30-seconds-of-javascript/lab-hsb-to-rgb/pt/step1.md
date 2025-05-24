# Conversão de HSB para RGB

Para converter uma tupla de cores HSB para o formato RGB, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use a [fórmula de conversão de HSB para RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) para converter para o formato apropriado.
- Os parâmetros de entrada devem estar na faixa de H: [0, 360], S: [0, 100], B: [0, 100].
- Todos os valores de saída devem estar na faixa de [0, 255].

Aqui está o código que você pode usar para converter HSB para RGB:

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

Por exemplo, se você deseja converter a tupla de cores HSB (18, 81, 99) para o formato RGB, você pode usar o seguinte código:

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
