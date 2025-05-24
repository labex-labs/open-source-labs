# JavaScript 를 사용하여 배열에서 고유한 값을 필터링하는 방법

JavaScript 를 사용하여 배열에서 고유한 값을 필터링하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Set` 생성자와 spread 연산자 (`...`) 를 사용하여 원래 배열의 고유한 값의 배열을 생성합니다.
3. `Array.prototype.filter()`를 사용하여 고유하지 않은 값만 포함하는 배열을 생성합니다.
4. 배열을 인수로 받아 위 단계를 적용하는 `filterUnique`라는 함수를 정의합니다.
5. 배열을 인수로 사용하여 `filterUnique` 함수를 호출합니다.

다음은 이를 달성하기 위한 코드 스니펫 예시입니다.

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

위 코드 스니펫에서 `filterUnique` 함수는 배열을 인수로 받아 `Set` 생성자와 `Array.prototype.filter()` 메서드를 적용하여 고유하지 않은 값만 있는 배열을 반환합니다.
