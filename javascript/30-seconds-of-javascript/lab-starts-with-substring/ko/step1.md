# 문자열이 부분 문자열로 시작하는지 확인하는 함수

주어진 문자열이 다른 문자열의 부분 문자열로 시작하는지 확인하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `for...in` 루프와 `String.prototype.slice()` 메서드를 사용하여 주어진 `word`의 각 부분 문자열을 처음부터 가져옵니다.
- `String.prototype.startsWith()` 메서드를 사용하여 현재 부분 문자열을 `text`와 비교합니다.
- 일치하는 부분 문자열이 발견되면 해당 부분 문자열을 반환합니다. 그렇지 않으면 `undefined`를 반환합니다.

다음은 이를 수행하는 JavaScript 함수입니다.

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

이 함수는 다음과 같이 호출할 수 있습니다.

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // returns '/>'
```
