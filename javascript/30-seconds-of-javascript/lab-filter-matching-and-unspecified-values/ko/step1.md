# 조건 및 키로 객체 필터링

조건에 따라 객체 배열을 필터링하고 지정되지 않은 키를 제거하려면 `reducedFilter()` 함수를 사용하십시오.

다음은 따라야 할 단계입니다.

1. `Array.prototype.filter()`를 사용하여 술어 (predicate) `fn`을 기반으로 배열을 필터링하여 조건이 참 (truthy) 값을 반환하는 객체를 반환합니다.

2. 필터링된 배열에 `Array.prototype.map()`을 사용하여 새 객체를 반환합니다.

3. `Array.prototype.reduce()`를 사용하여 `keys` 인수로 제공되지 않은 키를 필터링합니다.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

다음은 `reducedFilter()` 함수의 사용 예시입니다.

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Output: [{ id: 2, name: 'mike'}]
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
