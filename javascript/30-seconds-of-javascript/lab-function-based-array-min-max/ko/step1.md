# 제공된 함수를 사용하여 배열의 최소값과 최대값 찾는 방법

코딩 연습을 위해 터미널 또는 SSH 를 열고 `node`를 입력하세요.

다음은 비교 규칙을 설정하는 제공된 함수를 기반으로 배열의 최소값과 최대값을 반환하는 함수입니다.

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

사용하려면 다음 단계를 따르세요.

1. 처리하려는 배열과 선택적 `comparator` 함수를 사용하여 `reduceWhich`를 호출합니다.
2. `reduceWhich` 함수는 `Array.prototype.reduce()`를 `comparator` 함수와 함께 사용하여 배열에서 적절한 요소를 반환합니다.
3. 두 번째 인수 (`comparator`) 를 생략하면 기본 함수가 사용되며, 이는 배열에서 최소 요소를 반환합니다.

`reduceWhich`를 사용하는 몇 가지 예는 다음과 같습니다.

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

위의 예에서 `reduceWhich`에 대한 첫 번째 호출은 배열 `[1, 3, 2]`의 최소값인 `1`을 반환합니다. 두 번째 호출은 비교 순서를 반전시키는 `comparator` 함수를 기반으로 동일한 배열의 최대값을 반환합니다. 세 번째 호출은 객체의 `age` 속성을 비교하는 `comparator` 함수를 기반으로 `age` 속성이 최소인 배열의 객체를 반환합니다.
