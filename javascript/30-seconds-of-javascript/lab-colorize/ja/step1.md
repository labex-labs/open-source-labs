# テキストに色を付ける

コンソールに色付きのテキストを表示するには、以下の手順に従って `colorize()` 関数を使用します。

- ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- テンプレートリテラルと特殊文字を使用して、文字列出力に適切な色コードを追加します。
- 背景色を追加するには、文字列の末尾に背景色をリセットする特殊文字を含めます。

`colorize()` 関数は、黒、赤、緑、黄、青、マゼンタ、シアン、白の色コードを含む 16 個のプロパティを持つオブジェクトを作成します。また、テキストに背景色を追加するためのプロパティも持っています。

`colorize()` 関数を使用するには、色付けしたいテキストを引数として渡し、その後に色または背景色のプロパティを指定します。たとえば、`colorize('foo').red` は赤文字で 'foo' を表示します。

`console.log()` 関数を使用して、色付きのテキストをコンソールに表示します。

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
console.log(colorize("foo").red); // 'foo' (赤文字)
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' (青背景)
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' (最初の単語は黄文字、2 番目の単語は緑文字、両方の背景色は白)
```
