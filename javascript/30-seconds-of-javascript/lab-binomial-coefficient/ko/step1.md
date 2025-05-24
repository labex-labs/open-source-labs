# 이항 계수 계산 (Binomial Coefficient Calculation)

반복 없이, 순서에 상관없이 `n`개의 항목에서 `k`개의 항목을 선택하는 방법의 수를 계산하려면 다음 JavaScript 함수를 사용할 수 있습니다.

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 원하는 값으로 함수를 호출하십시오. 예를 들어:

```js
binomialCoefficient(8, 2); // 28
```

함수가 올바르게 작동하는지 확인하려면 다음 단계를 따르십시오.

1. `Number.isNaN()`을 사용하여 두 값 중 하나라도 `NaN`인지 확인합니다.
2. `k`가 `0`보다 작은지, `n`보다 크거나 같은지, `1` 또는 `n - 1`과 같은지 확인하고 적절한 결과를 반환합니다.
3. `n - k`가 `k`보다 작은지 확인하고 그 값을 적절하게 전환합니다.
4. `2`부터 `k`까지 루프를 돌면서 이항 계수를 계산합니다.
5. 계산 시 반올림 오류를 고려하기 위해 `Math.round()`를 사용합니다.
