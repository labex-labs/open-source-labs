# 배열에서 일치하는 요소 제거하기

주어진 조건을 기반으로 배열에서 특정 요소를 제거하려면 `remove` 함수를 사용할 수 있습니다. 이 함수는 주어진 함수가 `false`를 반환하는 요소를 제거하여 원래 배열을 변경합니다.

`remove` 함수를 사용하는 단계는 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()`를 사용하여 truthy 값을 반환하는 배열 요소를 찾습니다.
3. `Array.prototype.reduce()`를 사용하여 `Array.prototype.splice()`를 통해 요소를 제거합니다.
4. 콜백 함수는 세 개의 인수 (값, 인덱스, 배열) 와 함께 호출됩니다.

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

`remove` 함수를 사용하는 예는 다음과 같습니다.

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

이것은 제거된 요소가 포함된 새로운 배열을 반환합니다.
