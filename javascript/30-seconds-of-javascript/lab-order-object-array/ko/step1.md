# JavaScript 에서 객체 배열 정렬 방법

JavaScript 에서 객체 배열을 정렬하려면 `Array.prototype.sort()` 메서드와 `Array.prototype.reduce()` 메서드를 기본값 `0`으로 `props` 배열에 사용할 수 있습니다.

다음은 지정된 속성 및 순서를 기반으로 객체 배열을 정렬하는 예시 함수 `orderBy`입니다.

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

이 함수를 사용하려면 객체 배열, 정렬할 속성 배열, 그리고 선택적으로 순서 배열을 전달합니다. `orders` 배열이 제공되지 않으면 함수는 기본적으로 `'asc'`로 정렬합니다.

다음은 `orderBy` 함수를 사용하는 몇 가지 예시입니다.

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// 이름 오름차순 및 나이 내림차순으로 정렬
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// 이름 오름차순 및 나이 오름차순으로 정렬 (기본 순서)
orderBy(users, ["name", "age"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
