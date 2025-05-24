# JavaScript 에서 Map 을 객체로 변환하는 방법

JavaScript `Map`을 객체로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Map.prototype.entries()` 메서드를 사용하여 `Map`을 키 - 값 쌍의 배열로 변환합니다.
3. `Object.fromEntries()` 메서드를 사용하여 배열을 객체로 변환합니다.

다음은 `Map`을 객체로 변환하는 예시 코드 조각입니다.

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

함수를 테스트하려면 다음을 실행할 수 있습니다.

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
