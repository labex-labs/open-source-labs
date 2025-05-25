# 객체 배열에서 값 추출하기 지침

객체 배열에서 값을 추출하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`을 사용하여 객체 배열을 각 객체의 지정된 `key`의 값으로 매핑합니다.
3. 다음 함수를 구현합니다.

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. 객체 배열의 예시로 함수를 테스트합니다.

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

이렇게 하면 객체 배열에서 지정된 `key`에 해당하는 값의 배열이 반환됩니다.
