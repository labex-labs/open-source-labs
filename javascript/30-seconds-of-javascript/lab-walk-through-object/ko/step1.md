# 객체 키 순회 코드

주어진 객체의 모든 키 목록을 생성하려면 다음 단계를 사용하십시오.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 객체와 키 배열을 인수로 받는 `walk`라는 제너레이터 함수를 정의합니다. 재귀를 사용하여 객체의 모든 키를 순회합니다.

3. `walk` 함수 내부에서 `for...of` 루프와 `Object.keys()`를 사용하여 객체의 키를 반복합니다.

4. `typeof`를 사용하여 주어진 객체의 각 값이 객체 자체인지 확인합니다. 값이 객체인 경우, `yield*` 표현식을 사용하여 동일한 제너레이터 함수인 `walk`에 재귀적으로 위임하고 현재 `key`를 키 배열에 추가합니다.

5. 그렇지 않으면, 현재 경로와 주어진 `key`의 값을 나타내는 키 배열을 `yield`합니다.

6. `yield*` 표현식을 사용하여 `walk` 제너레이터 함수에 위임합니다.

다음은 코드입니다.

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

코드를 테스트하려면 객체를 생성하고 `walkThrough` 함수를 사용하여 모든 키 목록을 생성합니다.

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
