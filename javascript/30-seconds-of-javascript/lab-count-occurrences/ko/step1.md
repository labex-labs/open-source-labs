# JavaScript 에서 발생 횟수 세는 방법

JavaScript 배열에서 특정 값이 나타나는 횟수를 세려면 `Array.prototype.reduce()` 메서드를 사용할 수 있습니다.

다음은 그 방법입니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 코드를 복사하여 붙여넣습니다.

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. 위의 코드에서 `countOccurrences` 함수는 두 개의 인수를 받습니다: 검색할 배열과 계산할 값입니다.
4. `reduce()` 메서드는 배열의 각 요소를 반복하고 특정 값을 만날 때마다 카운터를 증가시키는 데 사용됩니다.
5. 함수를 테스트하려면 다음과 같이 배열과 값을 사용하여 호출합니다.

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

이렇게 하면 배열 `[1, 1, 2, 1, 2, 3]`에서 `1`이 나타나는 횟수인 `3`이 반환됩니다.
