# JavaScript 에서 값이 숫자인지 확인하기

JavaScript 에서 값이 숫자인지 확인하려면, `typeof` 연산자를 사용하여 값이 숫자 원시 타입 (number primitive) 으로 분류되는지 확인할 수 있습니다. `NaN`은 `typeof`가 `number`이고 자기 자신과 같지 않기 때문에, `NaN` 관련 문제를 방지하기 위해 `val === val`를 사용하여 값이 자기 자신과 같은지 여부를 확인할 수도 있습니다.

다음은 주어진 값이 숫자인지 확인하는 예시 함수입니다.

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
