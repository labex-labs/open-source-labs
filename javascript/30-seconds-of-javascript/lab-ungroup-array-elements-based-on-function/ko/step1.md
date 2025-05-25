# 함수 기반으로 배열 요소 그룹 해제하는 방법

`zip`으로 생성된 배열의 요소를 그룹 해제하고 함수를 적용해야 하는 경우 `unzipWith`를 사용할 수 있습니다. 구현 방법은 다음과 같습니다.

1. `Math.max()`와 스프레드 연산자 (`...`) 를 사용하여 배열에서 가장 긴 하위 배열을 가져오고 `Array.prototype.map()`을 사용하여 각 요소를 배열로 만듭니다.
2. `Array.prototype.reduce()`와 `Array.prototype.forEach()`를 사용하여 그룹화된 값을 개별 배열에 매핑합니다.
3. `Array.prototype.map()`과 스프레드 연산자 (`...`) 를 사용하여 `fn`을 각 개별 요소 그룹에 적용합니다.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

`unzipWith`를 사용하려면 터미널/SSH 를 열고 `node`를 입력합니다. 그런 다음 다음 예제를 실행할 수 있습니다.

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

이렇게 하면 `zip`으로 생성된 입력 배열의 요소를 그룹 해제하고 제공된 함수를 적용하여 요소의 배열이 생성됩니다.
