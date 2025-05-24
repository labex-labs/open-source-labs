# 조건 적용을 위한 When 함수 사용

특정 조건이 충족될 때 함수를 적용하려면 `when` 함수를 사용합니다. 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`when` 함수는 하나의 인수를 받아 인수가 truthy(참) 인 경우 콜백을 실행하고, falsy(거짓) 인 경우 인수를 반환하는 새로운 함수를 반환합니다. 이 함수는 단일 값 `x`를 예상하고, `pred` 매개변수를 기반으로 적절한 값을 반환합니다.

다음은 `when` 함수의 예시 구현입니다.

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

`when` 함수를 사용하여 짝수를 두 배로 만드는 새로운 함수를 만들 수 있습니다.

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
