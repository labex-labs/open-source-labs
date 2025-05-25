# Conversor de RGB para Hexadecimal

Para converter valores RGB em um código de cor hexadecimal:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a seguinte função:

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3.  Chame a função com os valores RGB como argumentos para obter um valor hexadecimal de 6 dígitos.

Por exemplo:

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
