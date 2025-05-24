# 문자열이 부분 문자열로 끝나는지 확인하는 함수

주어진 문자열이 다른 문자열의 부분 문자열로 끝나는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `for...in` 루프와 `String.prototype.slice()`를 사용하여 주어진 `word`의 각 부분 문자열을 끝에서부터 시작하여 가져옵니다.
3. `String.prototype.endsWith()`를 사용하여 현재 부분 문자열을 `text`와 비교합니다.
4. 일치하는 부분 문자열이 발견되면 반환합니다. 그렇지 않으면 `undefined`를 반환합니다.

위 단계를 구현하는 코드 조각은 다음과 같습니다.

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
