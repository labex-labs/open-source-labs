# JavaScript 를 사용하여 HSL 을 RGB 로 변환하기

HSL 형식의 색상 튜플을 RGB 로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. [HSL 에서 RGB 로의 변환 공식](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB)을 사용하여 색상 튜플을 적절한 형식으로 변환합니다.
3. 입력 매개변수가 다음 범위 내에 있는지 확인합니다: H: [0, 360], S: [0, 100], L: [0, 100].
4. 출력 값은 [0, 255] 범위 내에 있어야 합니다.

다음은 HSL 에서 RGB 로의 변환 공식에 대한 JavaScript 코드입니다.

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

함수를 사용하려면 H, S, L 값을 인수로 제공합니다.

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
