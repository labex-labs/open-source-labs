# 숫자가 소수인지 확인하는 함수

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 함수는 주어진 정수가 소수인지 확인합니다. 숫자가 소수인지 확인하는 단계는 다음과 같습니다.

1. `2`부터 주어진 숫자의 제곱근까지의 숫자를 확인합니다.
2. 그 중 하나라도 주어진 숫자를 나누면 `false`를 반환합니다.
3. 그 중 어떤 숫자도 주어진 숫자를 나누지 않으면, 숫자가 `2` 미만이 아닌 한 `true`를 반환합니다.

JavaScript 에서 이 함수를 구현하는 코드는 다음과 같습니다.

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

인수로 숫자를 전달하여 함수를 테스트할 수 있습니다.

```js
isPrime(11); // true
```
