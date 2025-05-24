# 플랫 이터레이터 (Flat Iterator) 설명

반복 가능한 객체를 반복하고 중첩된 반복 가능 객체를 평탄화하는 제너레이터를 만들려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 제너레이터 함수에서 재귀 (recursion) 를 사용합니다.
3. `for...of` 루프를 사용하여 주어진 반복 가능 객체의 값을 반복합니다.
4. `Symbol.iterator`를 사용하여 각 값이 반복 가능한 객체인지 확인합니다.
5. 반복 가능한 객체인 경우, `yield*` 표현식을 사용하여 동일한 제너레이터 함수에 재귀적으로 위임합니다.
6. 그렇지 않으면 현재 값을 `yield`합니다.

다음은 코드 예시입니다.

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

이 예제에서 `arr`는 중첩된 배열과 세트를 포함한 값의 배열입니다. `flatIterator` 제너레이터 함수는 이러한 중첩된 값을 평탄화하고 평탄화된 배열을 반환하는 데 사용됩니다.
