# 함수를 기반으로 두 배열의 합집합을 찾는 방법

Node.js 를 사용하여 함수를 기반으로 두 배열의 합집합을 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. `Array.prototype.findIndex()`를 사용하여 비교자가 `a`에서 일치하는 항목을 찾지 못하는 `a`의 모든 값과 `b`의 값을 사용하여 `Set`을 만듭니다.

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. `unionWith` 함수를 세 개의 인자 (첫 번째 배열, 두 번째 배열, 비교자 함수) 와 함께 호출합니다.
4. 이 함수는 제공된 비교자 함수를 사용하여 두 배열 중 하나 이상에 한 번 이상 존재하는 모든 요소를 반환합니다.
5. `unionWith` 함수를 호출하는 예는 다음과 같습니다.

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

이것은 두 배열의 합집합으로 `[1, 1.2, 1.5, 3, 0, 3.9]`를 반환합니다.
