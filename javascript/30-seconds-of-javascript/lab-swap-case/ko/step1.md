# JavaScript 에서 문자열의 대소문자 바꾸는 방법

JavaScript 에서 문자열의 대소문자를 바꾸려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. spread operator (`...`) 를 사용하여 입력 문자열 `str`을 문자 배열로 변환합니다.
3. `String.prototype.toLowerCase()`와 `String.prototype.toUpperCase()`를 사용하여 소문자를 대문자로, 대문자를 소문자로 변환합니다.
4. `Array.prototype.map()`을 사용하여 각 문자에 변환을 적용하고, `Array.prototype.join()`을 사용하여 문자를 다시 문자열로 결합합니다.
5. 문자열의 대소문자를 두 번 바꾸는 것이 반드시 원래 문자열을 반환하지는 않을 수 있습니다.

다음은 JavaScript 에서 문자열의 대소문자를 바꾸는 방법을 보여주는 코드 예제입니다.

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Output: 'hELLO WORLD!'
```
