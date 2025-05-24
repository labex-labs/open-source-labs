# 배열 고유 대칭 차이 함수

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하십시오. 다음 함수는 두 배열 간의 고유한 대칭 차이 (symmetric difference) 를 반환합니다. 이 함수는 두 배열 중 어느 쪽에서든 중복 값을 제거합니다.

이를 위해 각 배열에서 `Array.prototype.filter()` 및 `Array.prototype.includes()`를 사용하여 다른 배열에 포함된 값을 제거합니다. 결과를 기반으로 `Set`을 생성하여 중복 값을 제거합니다.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

아래와 같이 함수를 사용하십시오.

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
