# 배열 요소의 동일성 확인

배열의 모든 요소가 동일한지 확인하려면, 모든 요소를 첫 번째 요소와 비교하는 `Array.prototype.every()` 메서드를 사용할 수 있습니다.

구현 방법은 다음과 같습니다:

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

`strict comparison` 연산자 (엄격한 비교 연산자) 가 요소를 비교하는 데 사용됩니다. 이 연산자는 `NaN`의 자기 불평등을 고려하지 않습니다.

사용 예시:

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
