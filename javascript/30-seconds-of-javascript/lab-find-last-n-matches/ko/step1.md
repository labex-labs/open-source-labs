# 마지막 N 개 일치 항목 찾기 지침

특정 조건을 만족하는 마지막 `n`개의 요소를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 아래 제공된 `findLastN` 함수를 사용합니다.
3. `arr` 배열과 일치시키려는 요소에 대해 truthy 값을 반환하는 `matcher` 함수를 제공합니다.
4. 선택적으로, 반환하려는 일치 항목의 수 `n`을 제공할 수도 있습니다 (기본값은 1).
5. 함수는 마지막 요소부터 시작하여 `for` 루프를 사용하여 `arr`의 각 요소에 대해 `matcher` 함수를 실행합니다.
6. 요소가 `matcher` 조건을 만족하면, `Array.prototype.unshift()`를 사용하여 결과 배열에 추가됩니다. 이 메서드는 배열의 앞에 요소를 추가합니다.
7. 결과 배열의 길이가 `n`과 같아지면 함수는 결과를 반환합니다.
8. 일치하는 항목이 없거나 `n`이 일치하는 항목의 수보다 큰 경우, 빈 배열이 반환됩니다.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

다음은 `findLastN` 함수를 사용하는 몇 가지 예입니다.

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
