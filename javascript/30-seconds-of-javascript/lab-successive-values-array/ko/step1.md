# 연속 값의 배열

JavaScript 에서 연속 값의 배열을 생성하려면 `Array.prototype.reduce()` 메서드를 사용할 수 있습니다. 이 메서드는 함수를 누산기 (accumulator) 와 배열의 각 요소에 왼쪽에서 오른쪽으로 적용하고, 연속적으로 축소된 값들의 배열을 반환합니다.

다음은 `reduceSuccessive` 함수를 사용하여 주어진 함수를 주어진 배열에 적용하고 각 새로운 결과를 저장하는 방법입니다.

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

그런 다음 배열, 함수 및 누산기의 초기 값을 사용하여 `reduceSuccessive` 함수를 호출할 수 있습니다.

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

이 함수로 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
