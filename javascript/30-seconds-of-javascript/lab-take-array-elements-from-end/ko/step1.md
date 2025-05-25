# JavaScript 에서 배열의 끝에서 요소 제거하는 방법

JavaScript 에서 배열의 끝에서 요소를 제거하려면 `Array.prototype.slice()` 메서드를 사용할 수 있습니다. 방법은 다음과 같습니다.

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

이 함수는 원래 배열의 마지막 `n`개 요소로 구성된 새로운 배열을 생성합니다. 사용 방법은 다음과 같습니다.

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하십시오.
