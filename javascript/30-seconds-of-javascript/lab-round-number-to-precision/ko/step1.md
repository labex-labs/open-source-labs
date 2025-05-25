# JavaScript 에서 숫자를 주어진 정밀도로 반올림하는 방법은 다음과 같습니다:

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- `Math.round()`와 템플릿 리터럴을 사용하여 숫자를 지정된 자릿수로 반올림합니다.
- 정수로 반올림하려면 두 번째 인수 `decimals`를 생략합니다.
- 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
- 예를 들어, `round(1.005, 2)`는 `1.01`을 반환합니다.
