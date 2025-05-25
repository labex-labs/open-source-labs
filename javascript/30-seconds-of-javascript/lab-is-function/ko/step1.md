# 값이 함수인지 확인하기

값이 함수인지 확인하려면 `function` 기본형과 함께 `typeof` 연산자를 사용할 수 있습니다.

다음은 주어진 값이 함수인지 확인하는 함수의 예시입니다.

```js
const isFunction = (val) => typeof val === "function";
```

다음과 같이 사용할 수 있습니다.

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.
