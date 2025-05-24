# 객체 반전 함수

원본 객체를 변경하지 않고 객체의 키 - 값 쌍을 반전시키려면 `invertKeyValues` 함수를 사용하십시오.

- 터미널/SSH 에서 `invertKeyValues(obj, fn)`을 입력하여 함수를 호출합니다. 여기서 `obj`는 반전시킬 객체이고 `fn`은 반전된 키에 적용할 선택적 함수입니다.

- `Object.keys()` 및 `Array.prototype.reduce()` 메서드는 반전된 키 - 값 쌍을 가진 새 객체를 생성하는 데 사용되며, 함수가 제공되면 각 반전된 키에 적용됩니다.

- `fn`이 생략되면 함수는 함수가 적용되지 않은 반전된 키만 반환합니다.

- 이 함수는 각 반전된 값이 반전된 값을 생성하는 데 책임이 있는 키의 배열인 객체를 반환합니다.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

사용 예시:

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
