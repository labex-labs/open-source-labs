# 배열에서 일치하는 값 추출 방법

JavaScript 를 사용하여 배열에서 특정 값을 추출하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()`와 `Array.prototype.includes()`를 사용하여 필요 없는 값을 필터링하고 새로운 배열을 생성합니다.
3. `Array.prototype.length`를 설정하여 원래 배열의 길이를 `0`으로 재설정하여 변경합니다.
4. `Array.prototype.push()`를 사용하여 추출된 값만으로 원래 배열을 다시 채웁니다.
5. `Array.prototype.push()`를 사용하여 제거된 값을 새로운 배열에 추적합니다.

다음은 이러한 단계를 구현하는 예시 함수입니다.

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

이 함수를 사용하여 배열에서 특정 값을 제거하고 제거된 요소를 다음과 같이 반환할 수 있습니다.

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
