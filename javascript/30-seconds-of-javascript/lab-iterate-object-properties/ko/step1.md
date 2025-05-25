# JavaScript 에서 객체의 고유 속성을 반복하는 방법

객체의 고유 속성을 반복하고 코딩을 연습하려면 다음 단계를 따르세요.

1. 터미널 또는 SSH 를 엽니다.
2. `node`를 입력하여 새로운 Node.js 세션을 시작합니다.
3. `Object.keys()` 메서드를 사용하여 객체의 고유 속성 배열을 가져옵니다.
4. `Array.prototype.forEach()` 메서드를 사용하여 각 속성을 반복하고 제공된 함수를 실행합니다.
5. 제공된 함수는 세 개의 인수를 받아야 합니다: 속성 값, 속성 키 및 객체 자체.
6. 객체와 제공된 함수를 사용하여 `forOwn()` 함수를 사용하여 객체의 속성을 반복합니다.

다음은 코드 예제입니다.

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

이 코드는 `foo` 및 `a` 속성의 값을 콘솔에 기록합니다.
