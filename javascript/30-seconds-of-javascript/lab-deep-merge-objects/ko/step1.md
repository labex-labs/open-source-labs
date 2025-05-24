# JavaScript 에서 객체를 딥 머지하는 방법

JavaScript 에서 두 객체를 딥 머지하려면 `deepMerge` 함수를 사용할 수 있습니다. 이 함수는 두 개의 객체와 함수를 인수로 받습니다. 이 함수는 두 객체 모두에 존재하는 키를 처리하는 데 사용됩니다.

`deepMerge` 함수는 다음과 같이 작동합니다.

1. `Object.keys()`를 사용하여 두 객체의 키를 가져와서 `Set`을 생성하고, 스프레드 연산자 (`...`) 를 사용하여 모든 고유 키의 배열을 생성합니다.
2. `Array.prototype.reduce()`를 사용하여 각 고유 키를 객체에 추가하고, `fn`을 사용하여 주어진 두 객체의 값을 결합합니다.

다음은 `deepMerge` 함수의 코드입니다.

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

`deepMerge` 함수를 사용하려면 두 객체와 함수를 사용하여 호출합니다. 다음은 예시입니다.

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

이 예제에서 `deepMerge` 함수는 두 객체를 병합하는 데 사용됩니다. 결과 객체는 두 객체의 병합된 값을 갖습니다.
