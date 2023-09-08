# Colorize Text

To print colored text in the console, use the function `colorize()` by following the below steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use template literals and special characters to add the appropriate color code to the string output.
- To add a background color, include a special character that resets the background color at the end of the string.

The `colorize()` function creates an object with 16 properties, including the color codes for black, red, green, yellow, blue, magenta, cyan, and white. Additionally, it has properties for adding a background color to the text.

To use the `colorize()` function, call it with the text you want to colorize as the argument(s), followed by the color or background color property. For example, `colorize('foo').red` will print 'foo' with red letters.

Use the `console.log()` function to print the colored text to the console.

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
