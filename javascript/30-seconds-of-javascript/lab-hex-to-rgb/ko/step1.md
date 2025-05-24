# 16 진수에서 RGB 로 변환

16 진수 색상 코드 ( `#` 접두사 포함 여부와 관계없이) 를 RGB 문자열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 비트 오른쪽 시프트 연산자를 사용하고 `&` (and) 연산자로 비트를 마스크합니다.
3. 색상 코드가 3 자리인 경우, 먼저 6 자리 버전으로 변환합니다.
4. 6 자리 16 진수와 함께 알파 값이 제공되면 `rgba()` 문자열을 반환합니다.

다음은 변환을 위한 JavaScript 코드입니다.

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

다음 예제를 사용하여 `hexToRGB` 함수를 사용할 수 있습니다.

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
