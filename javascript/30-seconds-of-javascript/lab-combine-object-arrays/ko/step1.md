# 지정된 키를 기반으로 객체 배열을 결합하는 함수

특정 키를 기반으로 두 개의 객체 배열을 결합하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 주어진 `prop`을 기반으로 두 배열의 모든 객체를 결합하기 위해 객체 누산기 (accumulator) 와 함께 `Array.prototype.reduce()`를 사용합니다.
3. 결과 객체를 배열로 변환하고 반환하기 위해 `Object.values()`를 사용합니다.

다음은 사용할 수 있는 함수입니다.

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

이 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
