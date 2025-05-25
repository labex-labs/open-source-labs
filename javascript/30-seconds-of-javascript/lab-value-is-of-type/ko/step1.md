# 값의 유형 확인 함수

제공된 값이 지정된 유형인지 확인하려면 다음 단계를 따르세요.

- `Array.prototype.includes()`를 사용하여 값이 `undefined` 또는 `null`이 아닌지 확인합니다.
- `Object.prototype.constructor`를 사용하여 값의 constructor 속성을 지정된 `type`과 비교합니다.
- 아래의 `is()` 함수는 이러한 검사를 수행하고, 값이 지정된 유형인 경우 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

`is()`를 사용하여 값이 `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number`, 그리고 `Boolean`과 같은 다양한 유형인지 확인할 수 있습니다. 예를 들어:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
