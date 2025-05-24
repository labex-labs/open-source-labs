# JavaScript 에서 While 루프를 사용하여 배열을 초기화하고 채우는 방법

JavaScript 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`initializeArrayWhile` 함수는 조건이 충족되는 동안 함수에 의해 생성된 값으로 배열을 초기화하고 채웁니다. 작동 방식은 다음과 같습니다.

1. `arr`이라는 빈 배열, `i`라는 인덱스 변수, `el`이라는 요소를 생성합니다.
2. `conditionFn` 함수가 주어진 인덱스 `i`와 요소 `el`에 대해 `true`를 반환하는 동안 `mapFn` 함수를 사용하여 배열에 요소를 추가하기 위해 `while` 루프를 사용합니다.
3. `conditionFn` 함수는 현재 인덱스, 이전 요소 및 배열 자체, 세 개의 인수를 받습니다.
4. `mapFn` 함수는 현재 인덱스, 현재 요소 및 배열 자체, 세 개의 인수를 받습니다.
5. `initializeArrayWhile` 함수는 배열을 반환합니다.

다음은 코드입니다.

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

`initializeArrayWhile` 함수를 사용하여 배열을 초기화하고 값으로 채울 수 있습니다. 예를 들어:

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
