# 인수에 함수 호출하기

Node.js 를 사용하여 코드를 실행하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

제공된 각 함수를 수신하는 인수로 호출하고 결과를 반환하는 함수를 만들려면 다음을 수행하십시오.

- `Array.prototype.map()`과 `Function.prototype.apply()`를 사용하여 각 함수를 주어진 인수에 적용합니다.

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

예시:

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
