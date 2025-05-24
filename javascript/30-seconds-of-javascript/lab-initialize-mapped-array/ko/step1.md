# JavaScript 에서 매핑된 배열 초기화하기

JavaScript 에서 매핑된 배열을 초기화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array()` 생성자를 사용하여 원하는 길이의 배열을 생성합니다.
3. `Array.prototype.fill()`을 사용하여 배열을 `null` 값으로 채웁니다.
4. 제공된 함수 `mapFn`을 사용하여 `Array.prototype.map()`을 사용하여 배열을 원하는 값으로 채웁니다.
5. 각 요소를 해당 인덱스로 매핑하려면 두 번째 인수 `mapFn`을 생략합니다.

다음은 코드 스니펫 예시입니다.

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

`initializeMappedArray` 함수를 사용하여 원하는 값으로 매핑된 배열을 생성할 수 있습니다.

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
