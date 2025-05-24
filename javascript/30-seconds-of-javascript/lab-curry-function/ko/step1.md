# 함수 커링 (Currying)

함수를 커링하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용합니다.
3. 제공된 인수 (`args`) 의 수가 충분한지 확인합니다.
4. 충분하다면, 전달된 함수 `fn`을 호출합니다.
5. 그렇지 않다면, `Function.prototype.bind()`를 사용하여 나머지 인수를 예상하는 커링된 함수 `fn`을 반환합니다.
6. 가변 인수를 허용하는 함수 (가변 함수, 예: `Math.min()`) 를 커링하려면, 선택적으로 두 번째 매개변수 `arity`에 인수의 수를 전달할 수 있습니다.
7. 다음 코드를 사용합니다.

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

다음은 몇 가지 예입니다.

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
