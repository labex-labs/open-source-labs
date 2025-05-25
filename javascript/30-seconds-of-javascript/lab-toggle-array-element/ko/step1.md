# 배열 내 요소 토글 방법

배열 내 요소를 토글하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.includes()`를 사용하여 주어진 요소가 배열에 있는지 확인합니다.
3. 요소가 배열에 있으면 `Array.prototype.filter()`를 사용하여 제거합니다.
4. 요소가 배열에 없으면 스프레드 연산자 (`...`) 를 사용하여 추가합니다.
5. 배열과 값을 인수로 받는 `toggleElement` 함수를 사용하여 배열 내 요소를 토글합니다.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

이러한 단계를 따르면 JavaScript 를 사용하여 배열 내 요소를 쉽게 토글할 수 있습니다.
