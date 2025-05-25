# 최대 부분 배열 알고리즘

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 알고리즘은 숫자 배열 내에서 가장 큰 합을 가진 연속적인 부분 배열을 찾습니다. 이 알고리즘을 구현하려면 다음 단계를 따르세요.

- 탐욕적 접근 방식 (greedy approach) 을 사용하여 현재 `sum`과 현재 최대값인 `maxSum`을 추적합니다. 모든 값이 음수인 경우 가장 높은 음수 값을 반환하도록 `maxSum`을 `-Infinity`로 설정합니다.
- 최대 시작 인덱스 `sMax`, 최대 종료 인덱스 `eMax` 및 현재 시작 인덱스 `s`를 추적하기 위한 변수를 정의합니다.
- `Array.prototype.forEach()`를 사용하여 값을 반복하고 현재 값을 `sum`에 더합니다.
- 현재 `sum`이 `maxSum`보다 크면 인덱스 값과 `maxSum`을 업데이트합니다.
- `sum`이 `0` 미만이면 `0`으로 재설정하고 `s`의 값을 다음 인덱스로 업데이트합니다.
- `Array.prototype.slice()`를 사용하여 인덱스 변수로 표시된 부분 배열을 반환합니다.

다음은 알고리즘에 대한 JavaScript 코드입니다.

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

다음은 함수 사용 예시입니다.

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
