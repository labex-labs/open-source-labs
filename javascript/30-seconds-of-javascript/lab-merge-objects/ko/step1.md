# 객체 병합 함수

두 개 이상의 객체를 병합하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. `Array.prototype.reduce()`와 `Object.keys()`를 함께 사용하여 모든 객체와 키를 반복합니다.
3. `Object.prototype.hasOwnProperty()`와 `Array.prototype.concat()`을 사용하여 여러 객체에 존재하는 키의 값을 추가합니다.
4. 주어진 코드 조각을 사용하여 두 개 이상의 객체를 결합하여 새로운 객체를 생성합니다.

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

예를 들어, 다음 객체를 고려해 보세요.

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

`merge()` 함수를 사용하여 이 두 객체를 병합하면 다음과 같은 결과가 나타납니다.

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
