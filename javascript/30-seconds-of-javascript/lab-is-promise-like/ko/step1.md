# JavaScript Promise

객체가 Promise 와 유사한지 확인하려면 `isPromiseLike` 함수를 사용하십시오. 이 함수는 객체가 null 이 아니고, 타입이 object 또는 function 이며, function 인 `.then` 속성을 가지고 있는지 확인합니다.

`isPromiseLike`의 코드는 다음과 같습니다.

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

`isPromiseLike`를 사용하는 몇 가지 예는 다음과 같습니다.

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

JavaScript 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
