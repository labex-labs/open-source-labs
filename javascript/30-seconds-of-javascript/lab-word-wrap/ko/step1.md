# Word Wrap 문자열 사용 설명

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요.

이 코드는 문자열 분리 문자를 사용하여 주어진 문자 수로 문자열을 래핑합니다. 사용하려면 다음 단계를 따르세요.

1. `String.prototype.replace()`와 정규 표현식 (regular expression) 을 사용하여 `max` 문자에 가장 가까운 공백에 주어진 분리 문자를 삽입합니다.
2. 세 번째 인수 `br`에 대한 기본값 `'\n'`을 사용하지 않으려면, 이를 생략하고 자신만의 문자를 제공할 수 있습니다.

다음은 코드입니다.

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

다음은 사용 예시입니다.

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
