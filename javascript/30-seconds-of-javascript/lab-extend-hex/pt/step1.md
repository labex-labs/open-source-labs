# Como Estender um Código de Cor de 3 Dígitos para um Código de Cor de 6 Dígitos

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Você pode usar a seguinte função para estender um código de cor de 3 dígitos para um código de cor de 6 dígitos:

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

Para converter um código de cor hexadecimal RGB de 3 dígitos para a forma de 6 dígitos, siga estes passos:

- Use `Array.prototype.map()`, `String.prototype.split()` e `Array.prototype.join()` para juntar o array mapeado.
- Use `Array.prototype.slice()` para remover `#` do início da string, já que ele é adicionado uma vez.

Aqui estão alguns exemplos:

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
