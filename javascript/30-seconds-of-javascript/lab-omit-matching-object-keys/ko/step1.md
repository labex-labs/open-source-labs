# 콜백 함수를 기반으로 객체 키 제거하기

콜백 함수를 기반으로 객체 키를 제거하려면 `omitBy` 함수를 사용하십시오.

- `omitBy`는 주어진 함수에 대해 falsy 값을 반환하는 속성으로 구성된 객체를 생성합니다.
- `Object.keys()`와 `Array.prototype.filter()`는 `fn`이 truthy 값을 반환하는 키를 제거하는 데 사용됩니다.
- `Array.prototype.reduce()`는 필터링된 키를 해당 키 - 값 쌍을 가진 객체로 다시 변환합니다.
- 콜백 함수는 두 개의 인수를 받습니다: `value`와 `key`.
- 아래 예제는 `omitBy`를 사용하여 객체에서 숫자 키를 제거하는 방법을 보여줍니다.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
