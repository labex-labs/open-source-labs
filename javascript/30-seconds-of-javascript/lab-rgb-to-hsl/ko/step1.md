# RGB 를 HSL 로 변환하기

RGB 색상 튜플을 HSL 형식으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열어 코딩 연습을 시작합니다.
2. `node`를 입력하고 Enter 키를 누릅니다.
3. [RGB 를 HSL 로 변환하는 공식](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/)을 사용하여 적절한 형식으로 변환합니다.
4. 모든 입력 매개변수가 [0, 255] 범위 내에 있는지 확인합니다.
5. 결과 값은 H: [0, 360], S: [0, 100], L: [0, 100] 범위 내에 있어야 합니다.

다음은 JavaScript 에서 RGBToHSL 함수의 예시입니다.

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

다음은 RGBToHSL 함수를 사용하는 예시입니다.

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
