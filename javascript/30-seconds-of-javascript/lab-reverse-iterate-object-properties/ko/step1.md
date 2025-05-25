# 객체의 고유 속성을 역순으로 반복하는 방법

객체의 고유 속성을 역순으로 반복하고 각 속성에 대해 콜백을 실행하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 사용하여 객체의 모든 속성을 가져옵니다.
3. `Array.prototype.reverse()`를 사용하여 속성의 순서를 반대로 합니다.
4. `Array.prototype.forEach()`를 사용하여 각 키 - 값 쌍에 대해 제공된 함수를 실행합니다.
5. 콜백 함수는 값, 키 및 객체, 이렇게 세 개의 인수를 가져야 합니다.

다음은 코드입니다.

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

이 함수는 모든 객체 및 콜백 함수와 함께 사용할 수 있습니다. 예를 들어, `{ foo: 'bar', a: 1 }`의 값을 역순으로 로그하려면 다음 코드를 사용할 수 있습니다.

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
