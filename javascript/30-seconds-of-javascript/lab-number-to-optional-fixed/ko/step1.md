# 숫자를 고정 소수점 표기법으로 변환하기

후행 0 없이 숫자를 고정 소수점 표기법으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Number.prototype.toFixed()`를 사용하여 숫자를 고정 소수점 표기법 문자열로 변환합니다.
3. `Number.parseFloat()`를 사용하여 고정 소수점 표기법 문자열을 다시 숫자로 변환하여 후행 0 을 제거합니다.
4. 템플릿 리터럴을 사용하여 숫자를 문자열로 변환합니다.

예제 코드:

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

다양한 입력으로 함수를 테스트할 수 있습니다.

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
