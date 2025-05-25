# 값의 Null 여부 확인

JavaScript 에서 값이 `null`인지 확인하려면 엄격한 동등 연산자 (`===`) 를 사용합니다. 다음은 주어진 값이 `null`이면 `true`를 반환하고 그렇지 않으면 `false`를 반환하는 `isNull`이라는 함수를 정의하는 코드 예시입니다.

```js
const isNull = (val) => val === null;
```

이 함수를 테스트하려면 확인하려는 값을 인수로 전달하여 호출할 수 있습니다. 예를 들어, `isNull(null)`은 `true`를 반환합니다.
