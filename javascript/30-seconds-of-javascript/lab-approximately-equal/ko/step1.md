# JavaScript 에서 근사 숫자 동일성 확인하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 코드는 두 숫자가 서로 근사적으로 같은지 확인합니다. 이를 위해 다음을 수행합니다.

- `Math.abs()` 메서드를 사용하여 두 값의 절대 차이를 `epsilon`과 비교합니다.
- 세 번째 인수, `epsilon`을 제공하지 않으면 함수는 기본값 `0.001`을 사용합니다.

다음은 코드입니다.

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

함수를 테스트하려면 다음과 같이 두 개의 숫자를 인수로 호출할 수 있습니다.

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

`Math.PI / 2.0`이 `0.001`의 엡실론 (epsilon) 으로 `1.5708`과 근사적으로 같기 때문에 `true`를 반환합니다.
