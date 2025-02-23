# Conversión de hexadecimal a RGB

Para convertir un código de color hexadecimal (con o sin prefijo `#`) en una cadena RGB, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador de desplazamiento a la derecha bit a bit y enmascare los bits con el operador `&` (y).
3. Si el código de color tiene 3 dígitos, conviértalo primero a la versión de 6 dígitos.
4. Si se proporciona un valor alfa junto al código hexadecimal de 6 dígitos, devuelva una cadena `rgba()`.

A continuación, se muestra el código JavaScript para la conversión:

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

Puede utilizar la función `hexToRGB` con los siguientes ejemplos:

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
