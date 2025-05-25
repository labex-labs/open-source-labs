# JavaScript 에서 함수 인수 재정렬 방법

JavaScript 에서 함수 인수를 재정렬하려면 `rearg()` 함수를 사용할 수 있습니다. 먼저, 지정된 인덱스에 따라 인수가 정렬된 상태로 제공된 함수를 호출하는 함수를 만듭니다. `Array.prototype.map()`을 사용하여 `indexes`를 기반으로 인수를 재정렬할 수 있습니다. 그런 다음, spread operator (`...`) 를 사용하여 변환된 인수를 `fn`에 전달합니다.

`rearg()` 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

이 예제에서는 `rearg()`를 사용하여 다른 함수의 인수를 재정렬하는 새 함수를 만듭니다.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

위 코드에서 `function(a, b, c) { return [a, b, c]; }` 함수의 인수를 재정렬하는 새 함수 `rearged`를 만듭니다. `indexes` 인수는 인수가 재정렬되어야 하는 순서를 지정합니다. 이 경우 세 번째 인수가 먼저 오고, 첫 번째 인수가 두 번째로 오고, 두 번째 인수가 세 번째로 오도록 하려고 합니다. `rearged('b', 'c', 'a')`를 호출하면 재정렬된 인수로 원래 함수를 호출한 결과인 `['a', 'b', 'c']`가 반환됩니다.
