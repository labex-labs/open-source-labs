# Conversión de RGB a HSB

Para convertir una tupla de color RGB al formato HSB, puedes seguir estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la [fórmula de conversión de RGB a HSB](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) para convertir la tupla de color RGB al formato HSB adecuado.
3. El rango de los parámetros de entrada es [0, 255], mientras que los valores resultantes tienen un rango de:

- H: [0, 360]
- S: [0, 100]
- B: [0, 100]

Aquí está la función en JavaScript:

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

Puedes llamar a la función de la siguiente manera:

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
