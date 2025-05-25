# JavaScript 함수를 사용하여 HTTP 쿠키 파싱하기

JavaScript 에서 HTTP Cookie 헤더 문자열을 파싱하고 모든 쿠키 이름 - 값 쌍의 객체를 반환하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `String.prototype.split()`을 사용하여 키 - 값 쌍을 서로 분리합니다.
- `Array.prototype.map()` 및 `String.prototype.split()`을 사용하여 각 쌍에서 키와 값을 분리합니다.
- `Array.prototype.reduce()` 및 `decodeURIComponent()`를 사용하여 모든 키 - 값 쌍을 가진 객체를 생성합니다.

다음은 위의 단계를 구현하는 `parseCookie()` 함수의 예시입니다.

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

다음과 같이 함수를 테스트할 수 있습니다.

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
