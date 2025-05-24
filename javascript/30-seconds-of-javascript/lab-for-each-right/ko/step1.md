# 배열의 각 요소에 대해 역순으로 함수를 실행하는 방법

배열의 마지막 요소부터 시작하여 각 배열 요소에 대해 함수를 실행하려면 다음 단계를 따르세요.

1. `Array.prototype.slice()`를 사용하여 주어진 배열을 복제합니다.
2. `Array.prototype.reverse()`를 사용하여 복제된 배열을 역순으로 정렬합니다.
3. `Array.prototype.forEach()`를 사용하여 역순으로 정렬된 배열을 반복합니다.

다음은 예시 코드 조각입니다.

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

다음 코드를 실행하여 함수를 테스트할 수 있습니다.

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.
