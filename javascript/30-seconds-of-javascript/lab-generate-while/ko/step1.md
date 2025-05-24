# 조건이 참인 동안 값을 생성하는 제너레이터

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이렇게 하면 주어진 조건이 충족되는 동안 계속해서 새로운 값을 생성하는 제너레이터가 생성됩니다.

제너레이터는 현재 `val`을 초기화하는 데 사용되는 `seed` 값으로 초기화됩니다. 그런 다음 `while` 루프를 사용하여 현재 `val`로 호출된 `condition` 함수가 `true`를 반환하는 동안 반복합니다.

`yield` 키워드는 현재 `val`을 반환하고 선택적으로 새로운 시드 값인 `nextSeed`를 받기 위해 사용됩니다. `next` 함수는 현재 `val`과 `nextSeed`로부터 다음 값을 계산하는 데 사용됩니다.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

제너레이터를 사용하려면 `seed`, `condition`, `next` 함수를 사용하여 호출하십시오. 예를 들어, `[...generateWhile(1, v => v <= 5, v => ++v)]`를 호출하면 `[1, 2, 3, 4, 5]`가 반환됩니다.
