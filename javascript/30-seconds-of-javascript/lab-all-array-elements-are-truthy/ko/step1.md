# 모든 배열 요소가 참인지 확인하기

컬렉션의 모든 요소가 `true`인지 확인하려면 `Array.prototype.every()` 메서드를 사용할 수 있습니다. 이 메서드는 predicate 함수를 인수로 사용하며, 배열의 모든 요소에 대해 함수가 `true`로 평가되면 `true`를 반환합니다.

코드를 단순화하기 위해 배열과 선택적 predicate 함수를 인수로 사용하는 `all`이라는 함수를 사용할 수 있습니다. 이 함수는 `Array.prototype.every()`를 사용하여 제공된 함수를 기반으로 배열의 모든 요소가 `true`를 반환하는지 확인합니다. 함수가 제공되지 않으면 기본값으로 `Boolean`이 사용됩니다.

`all` 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
