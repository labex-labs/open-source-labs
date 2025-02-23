# Conversión de HSB a RGB

Para convertir una tupla de color HSB al formato RGB, sigue estos pasos:

- Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- Utiliza la [fórmula de conversión de HSB a RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) para convertir al formato adecuado.
- Los parámetros de entrada deben estar en el rango de H: [0, 360], S: [0, 100], B: [0, 100].
- Todos los valores de salida deben estar en el rango de [0, 255].

Aquí está el código que puedes utilizar para convertir HSB a RGB:

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

Por ejemplo, si quieres convertir la tupla de color HSB (18, 81, 99) al formato RGB, puedes utilizar el siguiente código:

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
