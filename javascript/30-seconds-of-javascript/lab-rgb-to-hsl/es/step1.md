# Conversión de RGB a HSL

Para convertir una tupla de color RGB al formato HSL, sigue estos pasos:

1. Abre la Terminal/SSH para comenzar a practicar la codificación.
2. Escribe `node` y pulsa Enter.
3. Utiliza la [fórmula de conversión de RGB a HSL](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/) para convertir al formato adecuado.
4. Asegúrate de que todos los parámetros de entrada estén dentro del rango de [0, 255].
5. Los valores resultantes deben estar dentro del rango de H: [0, 360], S: [0, 100], L: [0, 100].

Aquí hay un ejemplo de la función RGBToHSL en JavaScript:

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

Aquí hay un ejemplo de cómo utilizar la función RGBToHSL:

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
