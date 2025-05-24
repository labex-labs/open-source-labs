# 함수를 가변 인자 함수로 변환하기

배열을 인수로 받는 함수를 가변 인자 함수로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 모든 입력을 배열을 인수로 받는 함수로 수집하는 클로저를 반환합니다.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. `collectInto` 함수를 사용하여 함수를 가변 인자 함수로 변환합니다.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (after about 2 seconds)
```

이렇게 하면 함수에서 임의의 수의 인수를 받아 추가 처리를 위해 배열로 수집할 수 있습니다.
