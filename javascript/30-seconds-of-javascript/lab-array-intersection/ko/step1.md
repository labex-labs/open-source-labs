# 배열 교집합 찾기

두 배열 간의 공통 요소를 찾고 중복을 제거하려면 다음 코드를 사용하십시오.

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

이 코드를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 다음과 같이 두 개의 배열을 인수로 사용하여 `intersection` 함수를 호출하십시오.

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

이렇게 하면 중복이 제거된 두 배열 모두에 존재하는 요소를 포함하는 배열이 반환됩니다.
