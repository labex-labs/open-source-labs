# RGB 문자열을 배열로 변환하기

`rgb()` 색상 문자열을 값 배열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.match()`를 사용하여 숫자 값을 가진 3 개의 문자열 배열을 가져옵니다.
3. `Array.prototype.map()`을 `Number`와 함께 사용하여 숫자 값 배열로 변환합니다.

다음은 사용할 수 있는 코드입니다.

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

함수를 테스트하려면 다음과 같이 `rgb()` 색상 문자열을 인수로 사용하여 호출합니다.

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
