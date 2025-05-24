# 배열 대칭 차이 (Array Symmetric Difference)

두 배열 간의 대칭 차이를 찾고 중복 값을 포함하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 각 배열에서 `Set`을 생성하여 각 배열의 고유한 값을 얻습니다.
3. 각 배열에 대해 `Array.prototype.filter()`를 사용하여 다른 배열에 포함되지 않은 값만 유지합니다.

다음은 코드입니다.

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
