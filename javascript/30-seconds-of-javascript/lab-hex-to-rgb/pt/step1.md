# Conversão de Hexadecimal para RGB

Para converter um código de cor hexadecimal (com ou sem o prefixo `#`) em uma string RGB, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador bitwise de deslocamento para a direita e máscara de bits com o operador `&` (and).
3.  Se o código de cor tiver 3 dígitos, primeiro converta-o para a versão de 6 dígitos.
4.  Se um valor alfa for fornecido junto com o hexadecimal de 6 dígitos, retorne uma string `rgba()`.

Aqui está o código JavaScript para a conversão:

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

Você pode usar a função `hexToRGB` com os seguintes exemplos:

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
