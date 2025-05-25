# RGB to HSB 변환

RGB 색상 튜플을 HSB 형식으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. [RGB to HSB 변환 공식](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB)을 사용하여 RGB 색상 튜플을 적절한 HSB 형식으로 변환합니다.
3. 입력 매개변수 범위는 [0, 255]이며, 결과 값의 범위는 다음과 같습니다.

- H: [0, 360]
- S: [0, 100]
- B: [0, 100]

다음은 JavaScript 의 함수입니다.

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

다음과 같이 함수를 호출할 수 있습니다.

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
