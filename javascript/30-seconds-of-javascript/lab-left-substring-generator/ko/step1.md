# 코드 실습: 왼쪽 부분 문자열 생성기

주어진 문자열의 모든 왼쪽 부분 문자열을 생성하려면 아래 제공된 `leftSubstrGenerator` 함수를 사용하십시오.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 문자열 인수를 사용하여 함수를 입력하십시오.

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

이 함수는 문자열이 비어있는 경우 조기에 종료하기 위해 `String.prototype.length`를 사용하고, `for...in` 루프와 `String.prototype.slice()`를 사용하여 시작부터 주어진 문자열의 각 부분 문자열을 `yield`합니다.
