# 코드 연습: 배열에서 무작위 요소 가져오기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 다음 코드는 Fisher-Yates 알고리즘을 사용하여 배열을 섞고, 배열 크기까지 배열에서 고유한 키를 가진 `n`개의 무작위, 고유한 요소를 검색합니다.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

이 코드를 사용하려면 배열과 검색할 요소의 선택적 숫자 `n`으로 `sampleSize()`를 호출합니다. `n`이 제공되지 않으면 함수는 배열에서 무작위로 하나의 요소만 반환합니다.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
