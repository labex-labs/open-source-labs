# 한 집합이 다른 집합의 상위 집합인지 확인하는 함수

한 집합이 다른 집합의 상위 집합인지 확인하려면 `superSet()` 함수를 사용합니다. 먼저, 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다. 그런 다음 다음 단계를 사용합니다.

- `Set` 생성자를 사용하여 각 iterable 에서 새로운 `Set` 객체를 생성합니다.
- `Array.prototype.every()`와 `Set.prototype.has()`를 사용하여 두 번째 iterable 의 각 값이 첫 번째 iterable 에 포함되어 있는지 확인합니다.
- 이 함수는 첫 번째 iterable 이 중복 값을 제외하고 두 번째 iterable 의 상위 집합인 경우 `true`를 반환합니다. 그렇지 않으면 `false`를 반환합니다.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

`superSet()`을 두 개의 set 을 인수로 사용하여 한 set 이 다른 set 의 상위 집합인지 확인합니다.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
