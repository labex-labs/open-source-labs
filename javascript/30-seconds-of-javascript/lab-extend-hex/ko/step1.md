# 3 자리 색상 코드를 6 자리 색상 코드로 확장하는 방법

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 다음 함수를 사용하여 3 자리 색상 코드를 6 자리 색상 코드로 확장할 수 있습니다.

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

3 자리 RGB 표기법의 16 진수 색상 코드를 6 자리 형식으로 변환하려면 다음 단계를 따르세요.

- `Array.prototype.map()`, `String.prototype.split()`, `Array.prototype.join()`을 사용하여 매핑된 배열을 결합합니다.
- `#`이 한 번 추가되므로 `Array.prototype.slice()`를 사용하여 문자열 시작 부분에서 `#`을 제거합니다.

다음은 몇 가지 예입니다.

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
