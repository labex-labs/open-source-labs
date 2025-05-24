# HSL 색상의 밝기 변경 방법

`hsl()` 색상 문자열의 밝기 값을 변경하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. `String.prototype.match()`를 사용하여 `hsl()` 문자열에서 숫자 값을 가진 세 개의 문자열 배열을 가져옵니다.

3. `Array.prototype.map()`을 `Number`와 함께 사용하여 문자열을 숫자 값의 배열로 변환합니다.

4. `Math.max()` 및 `Math.min()`을 사용하여 밝기 값이 유효 범위 (0 에서 100 사이) 내에 있는지 확인합니다.

5. 템플릿 리터럴을 사용하여 업데이트된 밝기 값을 가진 새로운 `hsl()` 문자열을 생성합니다.

다음은 이러한 단계를 구현하는 코드 스니펫 예시입니다.

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

그런 다음 `changeLightness()` 함수를 델타 값과 `hsl()` 문자열로 호출하여 업데이트된 밝기 값을 가진 새로운 `hsl()` 문자열을 얻을 수 있습니다. 예를 들어:

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
