# 주어진 함수로 배열 요소가 같은지 확인하기

배열의 모든 요소가 같은지 확인하려면 `allEqualBy` 함수를 사용하십시오. 이 함수는 주어진 매핑 함수 `fn`을 배열 `arr`의 첫 번째 요소에 적용합니다. 그런 다음 `Array.prototype.every()`를 사용하여 `fn`이 배열의 모든 요소에 대해 첫 번째 요소와 동일한 값을 반환하는지 확인합니다. 이 함수는 엄격한 비교 연산자 (strict comparison operator) 를 사용하며, 이는 `NaN` 자체 비동등성을 고려하지 않습니다.

다음은 `allEqualBy`의 코드입니다.

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

`allEqualBy`는 다음과 같이 사용할 수 있습니다.

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

이 함수로 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
