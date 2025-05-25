# JavaScript 를 사용하여 지정된 범위 내에서 임의의 정수를 생성하는 방법

JavaScript 를 사용하여 지정된 범위 내에서 임의의 정수를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.random()` 메서드를 사용하여 0 과 1 사이의 임의의 숫자를 생성합니다.
3. 임의의 숫자에 범위의 최대값과 최소값의 차이를 곱한 다음 최소값을 결과에 더하여 원하는 범위로 매핑합니다.
4. `Math.floor()` 메서드를 사용하여 결과를 가장 가까운 정수로 내림합니다.

위 단계를 구현하는 예제 코드 조각은 다음과 같습니다.

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

그런 다음 원하는 최소값과 최대값으로 `randomIntegerInRange()` 함수를 호출하여 해당 범위 내에서 임의의 정수를 생성할 수 있습니다. 예를 들어:

```js
randomIntegerInRange(0, 5); // 2
```
