# 값이 부울인지 확인하기

JavaScript 에서 값이 부울 기본형 (boolean primitive) 인지 확인하려면 `typeof` 연산자를 `===` 비교 연산자와 함께 사용합니다.

```js
const isBoolean = (val) => typeof val === "boolean";
```

`isBoolean()` 함수를 사용하여 값이 부울인지 확인하는 방법의 예는 다음과 같습니다.

```js
isBoolean(null); // returns false
isBoolean(false); // returns true
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
