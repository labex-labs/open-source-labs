# Levenshtein Distance 알고리즘

두 문자열 간의 차이를 계산하려면 Levenshtein Distance 알고리즘을 사용할 수 있습니다. 방법은 다음과 같습니다.

1. 문자열 중 하나의 `length`가 0 이면, 다른 문자열의 `length`를 반환합니다.
2. 중첩된 `for` 루프를 사용하여 대상 및 소스 문자열의 문자를 반복합니다.
3. 대상 및 소스에서 각각 `i - 1` 및 `j - 1`에 해당하는 문자를 대체하는 비용을 계산합니다 (같으면 `0`, 그렇지 않으면 `1`).
4. `Math.min()`을 사용하여 2 차원 배열의 각 요소를 위쪽 셀에 1 을 더한 값, 왼쪽 셀에 1 을 더한 값, 또는 왼쪽 위 셀에 이전에 계산된 비용을 더한 값 중 최소값으로 채웁니다.
5. 생성된 배열의 마지막 행의 마지막 요소를 반환합니다.

이 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 사용할 수 있는 코드는 다음과 같습니다.

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
