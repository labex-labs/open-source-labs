# JavaScript 에서 2 차원 배열 초기화하기

JavaScript 에서 2 차원 배열을 초기화하려면 다음 코드를 사용할 수 있습니다.

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

이 코드는 `Array.from()`과 `Array.prototype.map()`을 사용하여 `height` 행의 배열을 생성합니다. 여기서 각 행은 `width` 길이를 가진 새로운 배열입니다. 또한 `Array.prototype.fill()`을 사용하여 배열의 모든 항목을 `value` 매개변수로 설정합니다. `value`가 제공되지 않으면 기본값은 `null`입니다.

다음과 같이 함수를 호출할 수 있습니다.

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

이렇게 하면 너비가 2, 높이가 2 이고 모든 값이 0 으로 설정된 2 차원 배열이 생성됩니다.
