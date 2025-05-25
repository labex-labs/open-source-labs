# 주어진 범위 내 거듭제곱 합을 계산하는 함수

지정된 범위 내의 모든 숫자 (양쪽 끝 포함) 의 거듭제곱 합을 계산하려면 다음 함수를 사용하십시오.

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

이 함수를 사용하는 방법은 다음과 같습니다.

- `sumPower(end)`를 호출하여 1 부터 `end`까지의 모든 숫자의 제곱 합을 계산합니다.
- `sumPower(end, power)`를 호출하여 1 부터 `end`까지의 모든 숫자의 `power` 거듭제곱 합을 계산합니다.
- `sumPower(end, power, start)`를 호출하여 `start`부터 `end`까지의 모든 숫자의 `power` 거듭제곱 합을 계산합니다.

두 번째 및 세 번째 인수 (`power` 및 `start`) 는 선택 사항이며, 제공되지 않으면 각각 기본값으로 `2`와 `1`이 사용됩니다.

예시:

```js
sumPower(10); // 385 반환 (1 부터 10 까지의 숫자의 제곱 합)
sumPower(10, 3); // 3025 반환 (1 부터 10 까지의 숫자의 세제곱 합)
sumPower(10, 3, 5); // 2925 반환 (5 부터 10 까지의 숫자의 세제곱 합)
```
