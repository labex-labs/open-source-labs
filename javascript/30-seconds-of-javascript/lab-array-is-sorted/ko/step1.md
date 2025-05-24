# 코드 연습: 배열이 정렬되었는지 확인하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 숫자 배열이 정렬되었는지 확인하는 함수입니다.

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

사용하려면 숫자 배열을 `isSorted()`에 전달하십시오. 함수는 배열이 오름차순으로 정렬된 경우 `1`, 내림차순으로 정렬된 경우 `-1`, 정렬되지 않은 경우 `0`을 반환합니다.

다음은 몇 가지 예입니다.

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
