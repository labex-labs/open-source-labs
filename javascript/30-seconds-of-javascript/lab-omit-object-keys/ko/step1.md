# 객체에서 키 제거하기

객체에서 특정 키를 제거하려면, 객체와 제거할 키의 배열을 인수로 받는 `omit` 함수를 사용합니다.

- `Object.keys()` 메서드는 객체의 모든 키를 가져오는 데 사용됩니다.
- `Array.prototype.filter()` 메서드는 키 목록에서 지정된 키를 제거하는 데 사용됩니다.
- 마지막으로, `Array.prototype.reduce()`는 나머지 키 - 값 쌍으로 새로운 객체를 생성하는 데 사용됩니다.

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

사용 예시:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
