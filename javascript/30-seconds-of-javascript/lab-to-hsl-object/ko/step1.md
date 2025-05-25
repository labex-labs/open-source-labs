# HSL 을 객체로 변환하기

`hsl()` 색상 문자열을 각 색상의 숫자 값을 가진 객체로 변환하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `String.prototype.match()`를 사용하여 숫자 값을 가진 3 개의 문자열 배열을 가져옵니다.
- `Array.prototype.map()`과 `Number`를 함께 사용하여 문자열을 숫자 값 배열로 변환합니다.
- 배열 구조 분해 할당 (array destructuring) 을 사용하여 값을 명명된 변수에 저장합니다.
- 명명된 변수에서 적절한 객체를 생성합니다.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

사용 예시:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
