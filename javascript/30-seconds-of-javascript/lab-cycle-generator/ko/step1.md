# 사이클 제너레이터 (Cycle Generator) 사용 설명

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 그런 다음, 주어진 배열을 무한히 반복하는 제너레이터를 생성합니다. 다음은 단계별 안내입니다.

1. `Generator.prototype.next()`가 호출될 때마다 값을 `yield`하는 종료되지 않는 `while` 루프를 사용합니다.
2. 다음 값의 인덱스를 얻기 위해 `Array.prototype.length`와 모듈 연산자 (`%`) 를 사용하고, 각 `yield` 문 뒤에 카운터를 증가시킵니다.

다음은 `cycleGenerator` 함수의 예시입니다.

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

그런 다음 다음과 같이 함수를 사용할 수 있습니다.

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

이 지침을 통해 모든 배열을 무한히 반복하는 사이클 제너레이터를 생성할 수 있습니다.
