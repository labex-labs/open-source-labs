# 주어진 조건을 만족하는 객체 키 선택 함수

주어진 조건을 만족하는 객체 키를 선택하려면 `pickBy()` 함수를 사용하십시오. 이 함수는 주어진 함수가 truthy 값을 반환하는 속성으로 구성된 새로운 객체를 생성합니다.

- `Object.keys()`와 `Array.prototype.filter()`를 사용하여 `fn`이 falsy 값을 반환하는 키를 제거합니다.
- `Array.prototype.reduce()`를 사용하여 필터링된 키를 해당 키 - 값 쌍을 가진 객체로 다시 변환합니다.
- 콜백 함수는 두 개의 인자 (value, key) 로 호출됩니다.

다음은 `pickBy()` 함수의 코드입니다.

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

이 함수를 사용하여 조건을 만족하는 키를 선택할 수 있습니다. 예를 들어:

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
