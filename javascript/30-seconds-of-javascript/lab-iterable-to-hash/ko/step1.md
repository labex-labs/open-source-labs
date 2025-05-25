# Iterable 을 Hash 로 변환하기

Iterable (객체 또는 배열) 을 hash (키가 지정된 데이터 저장소) 로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.values()`를 사용하여 iterable 의 값을 가져옵니다.
3. `Array.prototype.reduce()`를 사용하여 값을 반복하고 참조 값으로 키가 지정된 객체를 생성합니다.
4. iterable 과 선택적 key 매개변수를 사용하여 `toHash` 함수를 호출하여 참조 값을 지정합니다.

다음은 JavaScript 에서 `toHash` 함수의 예시 구현입니다.

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

`toHash` 함수를 서로 다른 iterable 과 key 로 호출하여 다양한 hash 를 생성할 수 있습니다. 예를 들어:

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
