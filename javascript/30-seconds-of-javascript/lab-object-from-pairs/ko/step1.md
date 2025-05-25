# 키 - 값 쌍으로부터 객체 생성하기

키 - 값 쌍으로부터 객체를 생성하려면 `objectFromPairs` 함수를 사용하십시오.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- 이 함수는 `Array.prototype.reduce()`를 사용하여 키 - 값 쌍을 생성하고 결합합니다.
- 더 간단한 구현을 위해 [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries)를 사용할 수도 있습니다.

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

사용 예시:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
