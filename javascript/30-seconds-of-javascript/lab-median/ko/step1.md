# 숫자 배열의 중앙값 계산 방법

숫자 배열의 중앙값을 계산하려면 다음 단계를 따르세요:

1. 배열의 중간 지점을 찾습니다.
2. `Array.prototype.sort()`를 사용하여 값을 정렬합니다.
3. `Array.prototype.length`가 홀수이면 중간 지점의 숫자를 반환합니다. 짝수이면 두 중간 숫자의 평균을 반환합니다.
4. 코딩을 연습하고 `node`를 사용하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 이 로직을 구현하는 코드 스니펫 예시입니다:

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

아래와 같이 숫자 배열과 함께 이 함수를 호출할 수 있습니다:

```js
median([5, 6, 50, 1, -5]); // 5
```
