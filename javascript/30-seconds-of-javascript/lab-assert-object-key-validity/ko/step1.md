# 객체 키 검증

객체의 모든 키가 지정된 `keys`와 일치하는지 확인하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `Object.keys()`를 사용하여 객체 `obj`의 키를 검색합니다.
- `Array.prototype.every()` 및 `Array.prototype.includes()`를 사용하여 객체의 각 키가 `keys` 배열에 포함되어 있는지 검증합니다.

다음은 구현 예시입니다.

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
