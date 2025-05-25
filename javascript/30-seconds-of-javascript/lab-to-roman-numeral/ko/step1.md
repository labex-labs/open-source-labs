# 정수를 로마 숫자로 변환하기

정수를 로마 숫자 표현으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. `toRomanNumeral()` 함수는 `1`에서 `3999` 사이의 값 (양쪽 포함) 을 허용합니다.

3. (로마 숫자 값, 정수) 형식의 2-값 배열을 포함하는 조회 테이블을 만듭니다.

4. `Array.prototype.reduce()`를 사용하여 `lookup`의 값을 반복하고 `num`을 해당 값으로 반복해서 나눕니다.

5. `String.prototype.repeat()`를 사용하여 로마 숫자 표현을 누산기에 추가합니다.

다음은 `toRomanNumeral()` 함수의 코드입니다.

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
