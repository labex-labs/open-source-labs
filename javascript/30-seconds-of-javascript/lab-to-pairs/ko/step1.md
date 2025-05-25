# 객체를 쌍으로 변환하기

객체를 키 - 값 쌍의 배열로 변환하려면 `toPairs` 함수를 사용하십시오. 코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`toPairs` 함수는 다음과 같은 방식으로 작동합니다.

- 먼저, 주어진 iterable 객체에 대해 `Symbol.iterator`가 정의되어 있는지 확인합니다.
- `Symbol.iterator`가 정의되어 있으면 `Array.prototype.entries()`를 사용하여 객체에 대한 iterator 를 가져온 다음 `Array.from()`을 사용하여 결과를 키 - 값 쌍 배열의 배열로 변환합니다.
- 객체에 대해 `Symbol.iterator`가 정의되어 있지 않으면 대신 `Object.entries()`를 사용합니다.

다음은 `toPairs` 함수의 코드입니다.

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

`toPairs` 함수는 다음과 같은 다양한 유형의 객체와 함께 사용할 수 있습니다.

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0', 's'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
