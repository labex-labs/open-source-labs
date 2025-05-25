# Luhn 검사

신용 카드 번호, IMEI 번호, National Provider Identifier (NPI) 번호와 같은 식별 번호의 유효성을 검사하기 위해 Luhn 알고리즘을 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()`, 그리고 `parseInt()` 메서드를 조합하여 숫자 배열을 얻습니다.
3. `Array.prototype.shift()`를 사용하여 마지막 숫자를 얻습니다.
4. `Array.prototype.reduce()`를 사용하여 Luhn 알고리즘을 구현합니다.
5. `sum`이 10 으로 나누어 떨어지면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 코드입니다.

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

다음 예제를 사용하여 Luhn 검사 함수를 테스트할 수 있습니다.

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
