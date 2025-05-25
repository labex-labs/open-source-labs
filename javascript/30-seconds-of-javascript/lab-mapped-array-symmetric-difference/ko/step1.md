# 매핑된 배열 대칭 차이 (Mapped Array Symmetric Difference)

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 제공된 함수를 두 배열의 각 요소에 적용한 후 두 배열 간의 대칭 차이를 반환합니다. 작동 방식은 다음과 같습니다.

- `fn`을 적용한 후 각 배열의 고유한 값을 얻기 위해 각 배열에서 `Set`을 생성합니다.
- 각 배열에서 `Array.prototype.filter()`를 사용하여 다른 배열에 포함되지 않은 값만 유지합니다.

`symmetricDifferenceBy` 함수의 코드는 다음과 같습니다.

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

`symmetricDifferenceBy`는 다음과 같이 사용할 수 있습니다.

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
