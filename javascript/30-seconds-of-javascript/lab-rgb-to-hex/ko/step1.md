# RGB to Hex 변환기

RGB 값을 16 진수 색상 코드로 변환하려면 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 함수를 사용합니다:

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3. RGB 값을 인수로 사용하여 함수를 호출하여 6 자리 16 진수 값을 얻습니다.

예를 들어:

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
