# JavaScript 에서 배열의 중복되지 않은 값 필터링 방법

JavaScript 에서 배열의 중복되지 않은 값을 필터링하려면 고유한 값만 포함하는 새 배열을 만들 수 있습니다. 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Set` 생성자와 spread operator (`...`) 를 사용하여 원래 배열의 고유한 값의 배열을 만듭니다.
3. `Array.prototype.filter()`를 사용하여 고유한 값만 포함하는 배열을 만듭니다.

다음은 이를 수행하는 예시 함수입니다.

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

이 함수를 모든 배열과 함께 사용하여 중복되지 않은 값을 필터링할 수 있습니다. 예를 들어:

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
