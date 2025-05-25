# JavaScript 에서 Powerset 생성 방법

JavaScript 에서 주어진 숫자 배열의 powerset 을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()` 메서드를 `Array.prototype.map()` 메서드와 결합하여 요소를 반복하고 모든 조합을 포함하는 배열로 결합합니다.
3. 다음 코드를 구현합니다.

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. powerset 을 생성하려면 `powerset()` 함수를 호출하고 배열을 인수로 전달합니다. 예를 들어:

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

이렇게 하면 주어진 배열의 모든 가능한 부분 집합을 포함하는 배열이 반환됩니다.
