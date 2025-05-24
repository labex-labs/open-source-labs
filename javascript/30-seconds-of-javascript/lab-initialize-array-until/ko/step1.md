# 조건이 충족될 때까지 배열을 초기화하는 방법

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

특정 조건이 충족될 때까지 함수에 의해 생성된 값으로 배열을 초기화하고 채우는 단계는 다음과 같습니다.

1. 빈 배열 `arr`, 인덱스 변수 `i`, 그리고 요소 `el`을 생성합니다.
2. `conditionFn` 함수가 주어진 인덱스 `i`와 요소 `el`에 대해 `true`를 반환할 때까지 `mapFn` 함수를 사용하여 `do...while` 루프를 사용하여 배열에 요소를 추가합니다.
3. `conditionFn` 함수는 현재 인덱스, 이전 요소 및 배열 자체의 세 가지 인수를 받습니다.
4. `mapFn` 함수는 현재 인덱스, 현재 요소 및 배열 자체의 세 가지 인수를 받습니다.

다음은 코드입니다.

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

`initializeArrayUntil` 함수를 사용하려면 두 개의 함수를 인수로 제공합니다.

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

이 코드는 10 보다 큰 첫 번째 숫자까지 피보나치 수열로 배열을 초기화합니다. `conditionFn` 함수는 현재 값이 10 보다 큰지 확인하고, `mapFn` 함수는 수열의 다음 숫자를 생성합니다.
