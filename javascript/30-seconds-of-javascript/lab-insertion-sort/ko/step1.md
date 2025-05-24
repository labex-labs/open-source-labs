# JavaScript 에서의 삽입 정렬 (Insertion Sort) 알고리즘

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 알고리즘은 삽입 정렬 방식을 사용하여 숫자 배열을 정렬합니다. 이 알고리즘을 구현하려면 다음 단계를 따르세요:

1. `Array.prototype.reduce()`를 사용하여 주어진 배열의 모든 요소를 반복합니다.
2. 누산기 (accumulator) 의 `length`가 `0`이면 현재 요소를 추가합니다.
3. `Array.prototype.some()`을 사용하여 올바른 위치가 발견될 때까지 누산기의 결과를 반복합니다.
4. `Array.prototype.splice()`를 사용하여 현재 요소를 누산기에 삽입합니다.

다음은 JavaScript 에서 삽입 정렬을 구현하는 코드입니다:

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

다음 코드로 알고리즘을 테스트할 수 있습니다:

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
