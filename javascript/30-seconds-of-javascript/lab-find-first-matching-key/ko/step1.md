# 테스트를 만족하는 첫 번째 키 찾기 함수

주어진 테스트 함수를 만족하는 객체의 첫 번째 키를 찾으려면 `findKey()` 함수를 사용합니다. 먼저, `Object.keys()`를 사용하여 모든 객체 속성을 가져옵니다. 그런 다음, `Array.prototype.find()`를 사용하여 각 키 - 값 쌍에 테스트 함수를 적용합니다. 테스트 함수는 값, 키 및 객체, 이렇게 세 개의 인수를 받아야 합니다. 이 함수는 테스트 함수를 만족하는 첫 번째 키를 반환하거나, 아무것도 찾을 수 없는 경우 `undefined`를 반환합니다.

다음은 `findKey()`의 예시 구현입니다.

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

`findKey()`를 사용하려면 객체와 테스트 함수를 인수로 전달합니다.

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

이 예제에서 `findKey()`는 `active` 속성의 값이 `true`인 객체의 첫 번째 키를 반환하며, 이는 `'barney'`입니다.
