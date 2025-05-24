# 특정 키를 기반으로 배열을 객체로 변환하기

특정 키를 기반으로 배열을 객체로 변환하고 각 값에서 해당 키를 제외하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `Array.prototype.reduce()`를 사용하여 제공된 배열에서 객체를 생성합니다.
- 객체 구조 분해 할당 (object destructuring) 을 사용하여 주어진 `key`의 값과 관련된 `data`를 추출한 다음, 키 - 값 쌍을 객체에 추가합니다.

다음은 예시 구현입니다.

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

그런 다음 다음과 같이 함수를 사용할 수 있습니다.

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
