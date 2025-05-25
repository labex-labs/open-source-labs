# JavaScript 에서 값이 심볼인지 확인하기

JavaScript 에서 값이 심볼 기본형인지 확인하려면 `typeof` 연산자를 사용할 수 있습니다. 다음은 사용할 수 있는 예제 코드 조각입니다.

```js
const isSymbol = (val) => typeof val === "symbol";
```

`isSymbol` 함수를 호출하고 심볼을 인수로 전달하여 `true`를 반환하는지 확인할 수 있습니다. 다음은 예시입니다.

```js
isSymbol(Symbol("x")); // true
```
