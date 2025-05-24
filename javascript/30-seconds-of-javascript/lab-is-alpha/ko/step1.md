# 문자열이 알파벳인지 확인하는 함수

문자열이 알파벳 문자만 포함하는지 확인하려면:

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `RegExp.prototype.test()`를 사용하여 주어진 문자열이 알파벳 정규 표현식 패턴과 일치하는지 확인합니다.
- 함수 `isAlpha`는 문자열을 인수로 받아 문자열이 알파벳 문자만 포함하면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 예시입니다:

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
