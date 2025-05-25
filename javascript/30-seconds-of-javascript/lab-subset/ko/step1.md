# 이터러블의 부분 집합이 다른 이터러블에 포함되어 있는지 확인하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 함수는 중복 값을 제외하고 첫 번째 이터러블이 두 번째 이터러블의 부분 집합인지 확인합니다.

이를 위해 다음을 수행할 수 있습니다.

- `Set` 생성자를 사용하여 각 이터러블에서 새로운 `Set` 객체를 생성합니다.
- `Array.prototype.every()`와 `Set.prototype.has()`를 사용하여 첫 번째 이터러블의 모든 값이 두 번째 이터러블에 포함되어 있는지 확인합니다.

다음은 예시 구현입니다.

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

비교할 두 개의 세트 (set) 를 전달하여 `subSet` 함수를 사용할 수 있습니다. 예를 들어:

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
