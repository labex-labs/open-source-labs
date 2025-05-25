# 배열 값 교체 또는 추가 방법

배열에서 항목을 교체하거나 존재하지 않는 경우 추가하려면 다음 단계를 따르세요.

1. 스프레드 연산자 (`...`) 를 사용하여 배열의 얕은 복사본을 만듭니다.
2. `Array.prototype.findIndex()`를 사용하여 제공된 비교 함수 `compFn`을 만족하는 첫 번째 요소의 인덱스를 찾습니다.
3. 그러한 요소가 없으면 `Array.prototype.push()`를 사용하여 새 값을 배열에 추가합니다.
4. 그렇지 않으면 `Array.prototype.splice()`를 사용하여 찾은 인덱스의 값을 새 값으로 교체합니다.

다음은 이 기능을 구현하는 방법의 예입니다.

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

이 함수는 다음과 같이 객체 배열과 함께 사용할 수 있습니다.

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
