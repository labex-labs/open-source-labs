# 오른쪽 부분 문자열 생성기

주어진 문자열의 모든 오른쪽 부분 문자열을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 문자열이 비어있는 경우 `String.prototype.length`를 사용하여 반복을 조기에 중단합니다.
3. `for...in` 루프와 `String.prototype.slice()`를 사용하여 주어진 문자열의 각 부분 문자열을 끝에서부터 `yield`합니다.

다음은 코드 조각입니다.

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

사용 예시:

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
