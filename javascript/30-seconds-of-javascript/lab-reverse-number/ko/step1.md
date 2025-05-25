# 숫자 뒤집기

JavaScript 를 사용하여 숫자를 뒤집으려면 다음 단계를 통해 `reverseNumber()` 함수를 사용할 수 있습니다.

1. `Object.prototype.toString()`을 사용하여 숫자 `n`을 문자열로 변환합니다.
2. `String.prototype.split()`, `Array.prototype.reverse()` 및 `Array.prototype.join()`을 사용하여 `n`의 뒤집힌 값을 문자열로 가져옵니다.
3. `parseFloat()`를 사용하여 문자열을 다시 숫자로 변환합니다.
4. `Math.sign()`을 사용하여 숫자의 부호를 유지합니다.

다음은 `reverseNumber()` 함수의 코드입니다.

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
