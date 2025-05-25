# 배열 값 필터링

predicate 함수를 기반으로 배열을 필터링하고 predicate 함수가 false 를 반환하는 값만 반환하려면 다음 단계를 따르세요.

1. `Array.prototype.filter()`를 predicate 함수 `pred`와 함께 사용합니다.
2. filter 메서드는 predicate 함수가 `false`를 반환하는 값만 반환합니다.
3. 일치하지 않는 값을 거부하려면 predicate 함수와 배열을 `reject()` 함수에 전달합니다.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

`reject()` 함수를 사용하는 몇 가지 예는 다음과 같습니다.

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

이 단계를 따르면 predicate 함수를 기반으로 배열을 쉽게 필터링하고 일치하지 않는 값을 거부할 수 있습니다.
