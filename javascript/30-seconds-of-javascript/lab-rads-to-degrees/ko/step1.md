# 라디안을 도 (degree) 로 변환하기

각도를 라디안에서 도 (degree) 로 변환하려면 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 공식을 사용합니다: `degrees = radians * (180 / Math.PI)`
3. 공식에서 `radians`를 변환하려는 값으로 바꿉니다.
4. 결과는 도 (degree) 단위가 됩니다.

다음은 예시입니다:

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

이 코드는 `π/2` 라디안을 `90` 도로 변환합니다.
