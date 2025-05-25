# 문자열이 대문자인지 확인하는 함수

문자열이 대문자인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력합니다.
3. `String.prototype.toUpperCase()`를 사용하여 주어진 문자열을 대문자로 변환하고 원래 문자열과 비교하는 함수 `isUpperCase()`를 사용합니다.
4. 문자열이 대문자이면 함수는 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 예제 코드입니다.

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
