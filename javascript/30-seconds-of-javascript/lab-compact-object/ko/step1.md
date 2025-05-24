# 객체 압축 알고리즘

객체 또는 배열에서 모든 falsy 값을 깊이 제거하려면 다음 알고리즘을 사용하십시오.

1. 재귀 (recursion) 를 사용하여 각 중첩된 객체 또는 배열에 대해 `compactObject()` 함수를 호출합니다.
2. `Array.isArray()`, `Array.prototype.filter()` 및 `Boolean()`을 사용하여 반복 가능한 데이터를 초기화합니다. 이는 희소 배열을 피하기 위해 수행됩니다.
3. `Object.keys()` 및 `Array.prototype.reduce()`를 사용하여 적절한 초기 값으로 각 키를 반복합니다.
4. `Boolean()`을 사용하여 각 키의 값의 truthiness 를 결정하고 truthy 인 경우 누산기 (accumulator) 에 추가합니다.
5. `typeof`를 사용하여 주어진 값이 `object`인지 확인하고 함수를 다시 호출하여 깊이 압축합니다.

다음은 `compactObject()` 함수의 코드입니다.

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

이 함수를 사용하려면 객체 또는 배열을 `compactObject()`에 인수로 전달합니다. 이 함수는 모든 falsy 값이 제거된 새로운 객체 또는 배열을 반환합니다.

예를 들어:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
