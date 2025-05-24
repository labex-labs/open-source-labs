# 범위 내에서 숫자를 제한하는 함수

지정된 범위 내에서 숫자를 제한하려면 `clampNumber` 함수를 사용합니다.

시작하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩을 연습하십시오.

`clampNumber` 함수는 `num`, `a`, `b`의 세 가지 매개변수를 받습니다. `num`을 경계 값 `a`와 `b`로 지정된 포괄적인 범위 내로 제한하고 결과를 반환합니다.

`num`이 범위 내에 있으면 함수는 `num`을 반환합니다. 그렇지 않으면 범위 내에서 가장 가까운 숫자를 반환합니다.

다음은 `clampNumber` 함수의 코드입니다.

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

다음은 이 함수를 사용하는 몇 가지 예입니다.

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
