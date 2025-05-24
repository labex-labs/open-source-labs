# 숫자를 디지털화하는 방법

JavaScript 에서 숫자를 디지털화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.abs()`를 사용하여 숫자의 부호를 제거합니다.
3. 숫자를 문자열로 변환하고 spread operator (`...`) 를 사용하여 숫자의 배열을 생성합니다.
4. `Array.prototype.map()`과 `parseInt()`를 사용하여 각 숫자를 정수로 변환합니다.

다음은 `digitize` 함수의 코드입니다.

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

사용 예시:

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
