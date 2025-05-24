# 주어진 조건이 충족될 때까지 값 생성하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 그런 다음, 주어진 조건이 충족될 때까지 새로운 값을 생성하는 제너레이터를 만들 수 있습니다.

이 제너레이터를 만들려면 다음 단계를 따르세요:

- `seed` 값을 사용하여 현재 `val`을 초기화합니다.
- 현재 `val`로 호출된 `condition` 함수가 `false`를 반환하는 동안 반복을 유지하기 위해 `while` 루프를 사용합니다.
- 현재 `val`을 반환하고, 선택적으로 새로운 seed 값인 `nextSeed`를 받기 위해 `yield` 키워드를 사용합니다.
- 현재 `val`과 `nextSeed`에서 다음 값을 계산하기 위해 `next` 함수를 사용합니다.

다음은 예시 코드 조각입니다:

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

적절한 인수로 호출하여 제너레이터를 사용할 수 있습니다. 예를 들어:

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

이것은 `val`이 `6`과 같을 때 `v > 5` 조건이 충족되므로 `1`부터 `5`까지의 값 배열을 생성합니다.
