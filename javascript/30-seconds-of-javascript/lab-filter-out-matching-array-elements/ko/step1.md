# JavaScript 에서 일치하는 배열 요소 필터링 방법

JavaScript 배열에서 하나 이상의 지정된 값을 가진 요소를 필터링하려면 다음 단계를 따르세요.

1. 터미널 또는 SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 제외할 값을 찾기 위해 `Array.prototype.includes()` 메서드를 사용합니다.
3. 제외된 요소가 있는 새 배열을 생성하기 위해 `Array.prototype.filter()` 메서드를 사용합니다.

다음은 예시 코드 조각입니다.

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

이 예제에서 `without` 함수는 배열 `arr`과 하나 이상의 인수 `args`를 받습니다. 이 함수는 `filter()` 메서드를 사용하여 `args`에 지정된 값과 일치하는 모든 요소를 제외하는 새 배열을 생성합니다. `includes()` 메서드는 값이 `args`에 있는지 확인하는 데 사용됩니다. 마지막으로, 함수는 제외된 요소가 있는 새 배열을 반환합니다.
