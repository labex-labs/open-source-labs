# 객체 키 매핑 함수

제공된 함수를 사용하여 객체의 키를 매핑하고 새로운 객체를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 사용하여 객체의 키를 반복합니다.
3. `Array.prototype.reduce()`를 사용하여 제공된 함수 (`fn`) 를 통해 동일한 값을 가지면서 매핑된 키를 가진 새로운 객체를 생성합니다.

다음은 `mapKeys` 함수의 예시 구현입니다.

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

다음과 같은 예시 입력을 사용하여 함수를 테스트할 수 있습니다.

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
