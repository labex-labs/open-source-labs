# 처음 N 개의 일치 항목 찾는 방법

특정 기준을 충족하는 처음 `n`개의 요소를 찾으려면 `findFirstN` 함수를 사용하십시오. 방법은 다음과 같습니다.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. `findFirstN` 함수를 사용하여 검색할 배열, 일치 함수, 찾을 일치 항목의 수 (지정하지 않으면 기본값은 1) 를 전달합니다.
4. `matcher` 함수는 `arr`의 각 요소에 대해 실행되며, truthy 값을 반환하면 해당 요소가 결과 배열에 추가됩니다.
5. `res` 배열의 길이가 `n`에 도달하면 함수는 결과 배열을 반환합니다.
6. 일치하는 항목이 없으면 빈 배열이 반환됩니다.

다음은 `findFirstN` 함수의 코드입니다.

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

다음은 사용 예시입니다.

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
