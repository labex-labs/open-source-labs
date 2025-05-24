# 모든 일치 항목 인덱스

배열에서 `val`의 모든 인덱스를 찾으려면 `Array.prototype.reduce()`를 사용하여 요소를 반복하고 일치하는 요소의 인덱스를 저장합니다. `val`이 한 번도 발생하지 않으면 빈 배열이 반환됩니다.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

사용 예시:

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이것은 모든 일치 항목의 인덱스입니다.
