# Undefined 값 확인하기

값이 undefined 인지 확인하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

- 엄격한 동등 연산자 (strict equality operator) 를 사용하여 `val`이 `undefined`와 같은지 확인합니다.

```js
const isUndefined = (val) => val === undefined;
```

```js
isUndefined(undefined); // true
```

이 코드는 지정된 값이 undefined 인지 확인합니다.
