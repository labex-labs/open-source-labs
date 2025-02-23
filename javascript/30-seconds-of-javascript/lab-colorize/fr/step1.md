# Coloriser le texte

Pour imprimer du texte coloré dans la console, utilisez la fonction `colorize()` en suivant les étapes suivantes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez des littéraux de gabarit et des caractères spéciaux pour ajouter le code de couleur approprié à la sortie de chaîne.
- Pour ajouter une couleur d'arrière-plan, incluez un caractère spécial qui réinitialise la couleur d'arrière-plan à la fin de la chaîne.

La fonction `colorize()` crée un objet avec 16 propriétés, y compris les codes de couleur pour le noir, le rouge, le vert, le jaune, le bleu, le magenta, le cyan et le blanc. De plus, elle a des propriétés pour ajouter une couleur d'arrière-plan au texte.

Pour utiliser la fonction `colorize()`, appelez-la avec le texte que vous voulez colorer en tant qu'argument(s), suivi de la propriété de couleur ou de couleur d'arrière-plan. Par exemple, `colorize('foo').red` imprimera 'foo' avec des lettres rouges.

Utilisez la fonction `console.log()` pour imprimer le texte coloré dans la console.

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
console.log(colorize("foo").red); // 'foo' (lettres rouges)
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' (arrière-plan bleu)
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' (premier mot en lettres jaunes, deuxième mot en lettres vertes, arrière-plan blanc pour les deux)
```
