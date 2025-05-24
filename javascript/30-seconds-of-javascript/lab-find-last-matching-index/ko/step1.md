# JavaScript 를 사용하여 배열에서 마지막 일치하는 요소의 인덱스를 찾는 방법

JavaScript 배열에서 특정 조건과 일치하는 마지막 요소의 인덱스를 찾으려면 `findLastIndex` 함수를 사용하십시오. 사용 방법은 다음과 같습니다.

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

`findLastIndex` 함수는 두 개의 인수를 받습니다: 검색할 배열과 각 요소를 테스트할 함수입니다. 작동 방식은 다음과 같습니다.

1. `Array.prototype.map()`을 사용하여 `[index, value]` 쌍의 새 배열을 생성합니다.
2. `Array.prototype.filter()`를 사용하여 `fn` 함수에서 제공하는 조건과 일치하지 않는 배열의 요소를 제거합니다.
3. `Array.prototype.pop()`을 사용하여 필터링된 배열의 마지막 요소를 가져옵니다.
4. 필터링된 배열이 비어 있으면 `-1`을 반환합니다.

`findLastIndex`를 사용하는 예는 다음과 같습니다.

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (value 3 의 인덱스)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (찾을 수 없을 때의 기본값)
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
