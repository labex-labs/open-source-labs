# 배열이 모든 값을 포함하는지 확인하는 함수

배열 `values`의 모든 요소가 다른 배열 `arr`에 포함되어 있는지 확인하려면 JavaScript 에서 `includesAll` 함수를 사용할 수 있습니다.

함수 사용을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`includesAll` 함수는 다음과 같이 작동합니다.

- `Array.prototype.every()` 및 `Array.prototype.includes()` 메서드를 사용하여 `values`의 모든 요소가 `arr`에 포함되어 있는지 확인합니다.
- `values`의 모든 요소가 `arr`에 포함되어 있으면 함수는 `true`를 반환합니다. 그렇지 않으면 `false`를 반환합니다.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

`includesAll` 함수를 사용하는 예는 다음과 같습니다.

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
