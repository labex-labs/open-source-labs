# 매핑을 통해 두 배열의 차이를 반환하는 함수

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 두 개의 배열을 인수로 받아 제공된 함수를 두 배열의 각 요소에 적용하여 차이를 반환합니다.

이를 위해 다음을 수행합니다.

- 두 번째 배열 (`b`) 의 각 요소에 함수 (`fn`) 를 적용하여 `Set`을 생성합니다.
- `Array.prototype.map()`을 사용하여 첫 번째 배열 (`a`) 의 각 요소에 함수 (`fn`) 를 적용합니다.
- `Array.prototype.filter()`를 첫 번째 배열 (`a`) 에 있는 함수 (`fn`) 와 함께 사용하여 두 번째 배열 (`b`) 에 포함되지 않은 값만 유지합니다. 이때 `Set.prototype.has()`를 사용합니다.

다음은 해당 함수의 코드입니다.

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

다음은 이 함수를 사용하는 몇 가지 예시입니다.

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
