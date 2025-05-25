# 주어진 범위 내에 숫자가 있는지 확인하는 함수

숫자가 지정된 범위 내에 속하는지 확인하려면 `inRange` 함수를 사용합니다. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.

`inRange` 함수를 사용하는 단계는 다음과 같습니다.

1. 산술 비교를 사용하여 주어진 숫자가 지정된 범위 내에 있는지 확인합니다.
2. 두 번째 인수 `end`가 지정되지 않은 경우, 범위는 `0`부터 `start`까지로 간주됩니다.
3. `inRange` 함수는 세 개의 인수 `n`, `start`, `end`를 받습니다.
4. `end`가 `start`보다 작으면 함수는 `start`와 `end`의 값을 바꿉니다.
5. `end`가 지정되지 않은 경우, 함수는 `n`이 0 보다 크거나 같고 `start`보다 작은지 확인합니다.
6. `end`가 지정된 경우, 함수는 `n`이 `start`보다 크거나 같고 `end`보다 작은지 확인합니다.
7. 함수는 `n`이 지정된 범위 내에 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 `inRange` 함수입니다.

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

다음은 `inRange` 함수를 사용하는 몇 가지 예입니다.

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
