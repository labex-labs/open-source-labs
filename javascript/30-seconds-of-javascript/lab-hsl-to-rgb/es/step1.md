# Convertir HSL a RGB usando JavaScript

Para convertir una tupla de color en formato HSL a RGB, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la [fórmula de conversión de HSL a RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB) para convertir la tupla de color al formato adecuado.
3. Asegúrate de que los parámetros de entrada estén dentro de los siguientes rangos: H: [0, 360], S: [0, 100], L: [0, 100].
4. Los valores de salida deben estar dentro del rango [0, 255].

Aquí está el código de JavaScript para la fórmula de conversión de HSL a RGB:

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

Para utilizar la función, proporciona los valores de H, S y L como argumentos:

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
