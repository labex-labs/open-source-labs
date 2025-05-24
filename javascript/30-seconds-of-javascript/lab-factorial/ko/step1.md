# 숫자의 팩토리얼 계산

숫자의 팩토리얼을 계산하려면 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용하여 팩토리얼을 계산합니다.
3. `n`이 1 보다 작거나 같으면 1 을 반환합니다.
4. 그렇지 않으면 `n`과 `n - 1`의 팩토리얼의 곱을 반환합니다.
5. `n`이 음수이면 `TypeError`를 발생시킵니다.

다음은 팩토리얼을 계산하는 코드입니다:

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

`factorial` 함수를 숫자를 인수로 사용하여 호출하여 코드를 테스트할 수 있습니다:

```js
factorial(6); // 720
```
