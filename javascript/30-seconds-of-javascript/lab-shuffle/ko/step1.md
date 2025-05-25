# 배열 섞기 알고리즘

JavaScript 에서 배열을 섞으려면 Fisher-Yates 알고리즘을 사용하십시오. 이 알고리즘은 배열의 요소를 무작위로 재정렬하고 새로운 배열을 반환합니다.

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

Fisher-Yates 알고리즘의 코드는 다음과 같습니다.

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

배열을 섞으려면 `shuffle` 함수에 배열을 전달하면 섞인 배열을 반환합니다. 예를 들어:

```js
const foo = [1, 2, 3];
shuffle(foo); // returns [2, 3, 1], and foo is still [1, 2, 3]
```
