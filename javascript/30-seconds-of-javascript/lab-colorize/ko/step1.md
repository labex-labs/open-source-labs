# 텍스트 색상 지정 (Colorize Text)

콘솔에 색상 텍스트를 출력하려면 아래 단계를 따라 `colorize()` 함수를 사용하십시오.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- 템플릿 리터럴 (template literals) 과 특수 문자를 사용하여 문자열 출력에 적절한 색상 코드를 추가합니다.
- 배경 색상을 추가하려면 문자열 끝에 배경 색상을 재설정하는 특수 문자를 포함합니다.

`colorize()` 함수는 검정, 빨강, 녹색, 노랑, 파랑, 자홍, 청록, 흰색에 대한 색상 코드를 포함하여 16 개의 속성을 가진 객체를 생성합니다. 또한 텍스트에 배경 색상을 추가하기 위한 속성도 있습니다.

`colorize()` 함수를 사용하려면 색상을 지정하려는 텍스트를 인수로 사용하여 호출한 다음 색상 또는 배경 색상 속성을 지정합니다. 예를 들어, `colorize('foo').red`는 'foo'를 빨간색 글자로 출력합니다.

`console.log()` 함수를 사용하여 색상 텍스트를 콘솔에 출력합니다.

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
