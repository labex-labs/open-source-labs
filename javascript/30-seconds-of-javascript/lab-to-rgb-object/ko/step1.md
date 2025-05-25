# RGB 를 객체로 변환하기

`rgb()` 색상 문자열을 각 색상의 값을 가진 객체로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.match()`를 사용하여 숫자 값을 가진 3 개의 문자열 배열을 가져옵니다.
3. `Array.prototype.map()`을 `Number`와 함께 사용하여 숫자 값의 배열로 변환합니다.
4. 배열 구조 분해 (array destructuring) 를 사용하여 값을 명명된 변수에 저장하고, 해당 변수들로부터 적절한 객체를 생성합니다.

다음은 사용할 수 있는 코드입니다.

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
