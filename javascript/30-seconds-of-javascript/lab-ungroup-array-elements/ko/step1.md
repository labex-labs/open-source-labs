# JavaScript 에서 배열 요소 그룹 해제 방법

`zip` 함수로 생성된 배열의 요소를 그룹 해제하려면 JavaScript 에서 `unzip` 함수를 사용하여 배열의 배열을 만들 수 있습니다. 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.max()`, `Function.prototype.apply()`를 사용하여 배열에서 가장 긴 하위 배열을 얻고, `Array.prototype.map()`을 사용하여 각 요소를 배열로 만듭니다.
3. `Array.prototype.reduce()`와 `Array.prototype.forEach()`를 사용하여 그룹화된 값을 개별 배열에 매핑합니다.

`unzip` 함수의 코드는 다음과 같습니다.

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

다음 예제와 함께 `unzip` 함수를 사용할 수 있습니다.

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

이 단계를 따르면 JavaScript 에서 배열 요소를 쉽게 그룹 해제할 수 있습니다.
