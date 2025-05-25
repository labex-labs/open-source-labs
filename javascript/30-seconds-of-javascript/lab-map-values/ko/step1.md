# 객체 값 매핑 함수

제공된 함수를 사용하여 객체의 값을 매핑하여 동일한 키를 가진 새로운 객체를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 사용하여 객체의 키를 반복합니다.
3. `Array.prototype.reduce()`를 사용하여 제공된 함수 `fn`을 사용하여 동일한 키와 매핑된 값을 가진 새로운 객체를 생성합니다.
4. 아래 코드는 `mapValues` 함수의 구현을 보여줍니다.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

다음은 `mapValues` 함수의 사용 예시입니다.

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
