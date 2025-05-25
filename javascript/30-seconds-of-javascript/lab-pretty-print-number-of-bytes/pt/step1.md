# Converter Bytes para String Legível por Humanos

Para converter um número em bytes para uma string legível por humanos, use a função `prettyBytes()`. Aqui estão algumas coisas a ter em mente:

- A função usa um array (dicionário) de unidades para ser acessado com base no expoente.
- Você pode usar o segundo argumento, `precision` (precisão), para truncar o número para um certo número de dígitos. O valor padrão é `3`.
- Você pode usar o terceiro argumento, `addSpace` (adicionarEspaço), para adicionar um espaço entre o número e a unidade. O valor padrão é `true`.
- A função retorna a string formatada, construindo-a, levando em consideração as opções fornecidas e se é negativa ou não.

Aqui está o código para a função `prettyBytes()`:

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

E aqui estão alguns exemplos de como usar a função `prettyBytes()`:

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
