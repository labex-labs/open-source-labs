# JavaScript 에서 배열에서 무작위 요소 가져오는 방법

JavaScript 에서 배열에서 무작위 요소를 가져오려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.random()` 메서드를 사용하여 0 과 1 사이의 무작위 숫자를 생성합니다.
3. `Array.prototype.length`를 사용하여 무작위 숫자에 배열의 길이를 곱합니다.
4. `Math.floor()`를 사용하여 결과를 가장 가까운 정수로 반올림합니다.
5. 반올림된 숫자를 인덱스로 사용하여 배열에서 무작위 요소에 접근합니다.
6. 이 방법은 문자열에도 적용됩니다.

다음은 이 접근 방식을 보여주는 코드 조각입니다.

```js
const getRandomElement = (arr) => arr[Math.floor(Math.random() * arr.length)];
```

`getRandomElement` 함수를 모든 배열과 함께 사용하여 무작위 요소를 얻을 수 있습니다. 예를 들어:

```js
getRandomElement([3, 7, 9, 11]); // 9
```
