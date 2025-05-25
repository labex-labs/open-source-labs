# Repeat Generator 를 사용한 코드 연습

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하여 주어진 값을 무한정 반복하는 제너레이터 (generator) 를 생성합니다. 종료되지 않는 `while` 루프를 사용하여 `Generator.prototype.next()`가 호출될 때마다 값을 `yield`합니다. 그런 다음, 전달된 값이 `undefined`가 아닌 경우 `yield` 문의 반환 값을 사용하여 반환된 값을 업데이트합니다.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

제너레이터를 테스트하려면 값 `5`를 사용하여 인스턴스를 생성하고 `repeater.next()`를 호출하여 시퀀스의 다음 값을 가져옵니다. 출력은 `{ value: 5, done: false }`가 됩니다. `repeater.next()`를 다시 호출하면 동일한 값이 반환됩니다. 값을 변경하려면 `repeater.next(4)`를 호출하면 `{ value: 4, done: false }`가 반환됩니다. 마지막으로 `repeater.next()`를 호출하면 업데이트된 값 `{ value: 4, done: false }`가 반환됩니다.
