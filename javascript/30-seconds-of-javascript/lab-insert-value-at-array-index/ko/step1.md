# JavaScript 를 사용하여 배열의 특정 인덱스에 값 삽입하는 방법

JavaScript 를 사용하여 배열의 특정 인덱스에 값을 삽입하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 적절한 인덱스와 삭제 개수 (delete count) `0`을 사용하여 `Array.prototype.splice()` 메서드를 사용하고, 삽입할 주어진 값을 spread 합니다.
3. `insertAt` 함수는 배열, 인덱스, 그리고 지정된 인덱스 뒤에 삽입할 하나 이상의 값을 받습니다.
4. 이 함수는 원본 배열을 변경하고 수정된 배열을 반환합니다.

다음은 `insertAt` 함수의 예시입니다.

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

위의 예시에서 `insertAt` 함수는 `myArray` 배열의 두 번째 인덱스 뒤에 값 `5`를 삽입하고, `otherArray` 배열의 첫 번째 인덱스 뒤에 값 `4`, `6`, `8`을 삽입하는 데 사용됩니다.
