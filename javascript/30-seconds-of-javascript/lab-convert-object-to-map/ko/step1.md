# 객체를 Map 으로 변환하는 방법

객체를 `Map`으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.entries()`를 사용하여 객체를 키 - 값 쌍의 배열로 변환합니다.
3. `Map` 생성자를 사용하여 배열을 `Map`으로 변환합니다.

다음은 예시 코드 조각입니다.

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

`objectToMap()` 함수를 사용하여 객체를 `Map`으로 변환할 수 있습니다. 예를 들어:

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
