# Cómo cambiar la claridad de un color HSL

Para cambiar el valor de claridad de una cadena de color `hsl()`, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice `String.prototype.match()` para obtener una matriz de tres cadenas con los valores numéricos de la cadena `hsl()`.

3. Utilice `Array.prototype.map()` en combinación con `Number` para convertir las cadenas en una matriz de valores numéricos.

4. Asegúrese de que el valor de claridad se encuentre dentro del rango válido (entre `0` y `100`) utilizando `Math.max()` y `Math.min()`.

5. Utilice una literal de plantilla para crear una nueva cadena `hsl()` con el valor de claridad actualizado.

A continuación, se muestra un fragmento de código de ejemplo que implementa estos pasos:

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

Luego, puede llamar a la función `changeLightness()` con un valor de delta y una cadena `hsl()` para obtener una nueva cadena `hsl()` con el valor de claridad actualizado. Por ejemplo:

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
