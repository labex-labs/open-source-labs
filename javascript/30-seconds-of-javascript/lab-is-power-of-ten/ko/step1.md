# 숫자가 10 의 거듭제곱인지 확인하기

숫자가 10 의 거듭제곱인지 확인하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`n`이 10 의 거듭제곱인지 확인하는 데 사용할 수 있는 코드는 다음과 같습니다.

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

`isPowerOfTen()` 함수를 사용하여 주어진 숫자가 10 의 거듭제곱인지 확인합니다.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
