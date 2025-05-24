# Colorir Texto

Para imprimir texto colorido no console, use a função `colorize()` seguindo os passos abaixo:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use literais de template e caracteres especiais para adicionar o código de cor apropriado à saída da string.
- Para adicionar uma cor de fundo, inclua um caractere especial que redefine a cor de fundo no final da string.

A função `colorize()` cria um objeto com 16 propriedades, incluindo os códigos de cor para preto, vermelho, verde, amarelo, azul, magenta, ciano e branco. Adicionalmente, possui propriedades para adicionar uma cor de fundo ao texto.

Para usar a função `colorize()`, chame-a com o texto que você deseja colorir como argumento(s), seguido pela propriedade de cor ou cor de fundo. Por exemplo, `colorize('foo').red` imprimirá 'foo' com letras vermelhas.

Use a função `console.log()` para imprimir o texto colorido no console.

```js
const colorize = (...args) => ({
  black: `\x1b[30m${args.join(" ")}`,
  red: `\x1b[31m${args.join(" ")}`,
  green: `\x1b[32m${args.join(" ")}`,
  yellow: `\x1b[33m${args.join(" ")}`,
  blue: `\x1b[34m${args.join(" ")}`,
  magenta: `\x1b[35m${args.join(" ")}`,
  cyan: `\x1b[36m${args.join(" ")}`,
  white: `\x1b[37m${args.join(" ")}`,
  bgBlack: `\x1b[40m${args.join(" ")}\x1b[0m`,
  bgRed: `\x1b[41m${args.join(" ")}\x1b[0m`,
  bgGreen: `\x1b[42m${args.join(" ")}\x1b[0m`,
  bgYellow: `\x1b[43m${args.join(" ")}\x1b[0m`,
  bgBlue: `\x1b[44m${args.join(" ")}\x1b[0m`,
  bgMagenta: `\x1b[45m${args.join(" ")}\x1b[0m`,
  bgCyan: `\x1b[46m${args.join(" ")}\x1b[0m`,
  bgWhite: `\x1b[47m${args.join(" ")}\x1b[0m`
});
```

```js
console.log(colorize("foo").red); // 'foo' (red letters)
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' (blue background)
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' (first word in yellow letters, second word in green letters, white background for both)
```
