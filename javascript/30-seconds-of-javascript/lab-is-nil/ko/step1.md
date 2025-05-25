# JavaScript 에서 값이 Null 또는 Undefined 인지 확인하는 방법

JavaScript 에서 값이 `null` 또는 `undefined`인지 확인하려면 엄격한 동등 연산자 (`===`) 를 사용할 수 있습니다. 다음은 지정된 값이 `null` 또는 `undefined`인지 확인하는 코드 예제입니다.

```js
const isNil = (val) => val === undefined || val === null;
```

이 함수를 사용하여 값이 `null` 또는 `undefined`인지 확인할 수 있습니다. 예시:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

JavaScript 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
