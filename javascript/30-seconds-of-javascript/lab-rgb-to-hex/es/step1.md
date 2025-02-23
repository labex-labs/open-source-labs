# Conversor de RGB a Hexadecimal

Para convertir valores RGB a un código de color hexadecimal:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la siguiente función:

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3. Llame a la función con los valores RGB como argumentos para obtener un valor hexadecimal de 6 dígitos.

Por ejemplo:

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
