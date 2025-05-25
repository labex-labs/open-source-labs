# 특정 범위 내에서 랜덤 정수 배열 생성하기

특정 범위 내에서 랜덤 정수 배열을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.from()`을 사용하여 원하는 길이의 빈 배열을 생성합니다.
3. `Math.random()`을 사용하여 랜덤 숫자를 생성하고 이를 지정된 범위에 매핑합니다. `Math.floor()`를 사용하여 정수로 변환합니다.
4. 함수 `randomIntArrayInRange()`는 세 개의 인수를 받습니다: `min`, `max`, 그리고 선택적 인수 `n` (기본값은 1).
5. 원하는 `min`, `max`, 및 `n` 값을 사용하여 `randomIntArrayInRange()` 함수를 호출하여 랜덤 정수 배열을 생성합니다.

다음은 코드입니다:

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

사용 예시:

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
