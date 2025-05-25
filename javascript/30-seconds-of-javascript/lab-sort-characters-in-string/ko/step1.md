# 문자열의 문자를 정렬하는 방법:

다음 코드를 사용하여 문자열의 문자를 알파벳 순으로 정렬합니다.

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

시작하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하십시오.

사용 예시:

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
