# 함수를 기반으로 배열을 두 개로 분할하는 방법

제공된 함수를 기반으로 배열을 두 개로 분할하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 두 개의 배열로 구성된 배열을 생성합니다.
3. `fn`이 `true`를 반환하는 요소는 첫 번째 배열에, `fn`이 `false`를 반환하는 요소는 두 번째 배열에 `Array.prototype.push()`를 사용하여 추가합니다.

다음은 사용할 수 있는 코드입니다.

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

이 코드를 테스트하려면 다음 예제를 사용할 수 있습니다.

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

이렇게 하면 두 개의 배열로 구성된 배열이 반환됩니다. 여기서 첫 번째 배열에는 제공된 함수가 `true`를 반환하는 모든 요소가 포함되고, 두 번째 배열에는 제공된 함수가 `false`를 반환하는 모든 요소가 포함됩니다.
