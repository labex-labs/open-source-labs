# 숫자 유효성 검사 함수

주어진 입력이 숫자인지 유효성을 검사하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `parseFloat()`를 사용하여 입력을 숫자로 변환해 봅니다.
- `Number.isNaN()`과 논리 부정 연산자 (`!`) 를 사용하여 입력이 숫자인지 확인합니다.
- `Number.isFinite()`를 사용하여 입력이 유한한지 확인합니다.
- `Number`와 느슨한 동등 연산자 (`==`) 를 사용하여 강제 변환 (coercion) 이 유효한지 확인합니다.

다음은 `validateNumber` 함수의 코드입니다.

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

`validateNumber` 함수는 다음과 같이 사용할 수 있습니다.

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
