# 인덱스에서 배열의 값 가져오는 방법

특정 인덱스에서 배열의 특정 값을 가져오려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()` 및 `Array.prototype.includes()`를 사용하여 필요 없는 값을 필터링하고 `removed`라는 새 배열에 저장합니다.
3. `Array.prototype.length`를 `0`으로 설정하여 길이를 재설정하여 원래 배열을 변경합니다.
4. `Array.prototype.push()`를 사용하여 가져온 값만으로 원래 배열을 다시 채웁니다.
5. `Array.prototype.push()`를 사용하여 제거된 값을 추적합니다.
6. `pullAtIndex` 함수는 두 개의 인수를 받습니다: 원래 배열과 가져올 인덱스 배열입니다.
7. 이 함수는 제거된 값의 배열을 반환합니다.

사용 예시:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
