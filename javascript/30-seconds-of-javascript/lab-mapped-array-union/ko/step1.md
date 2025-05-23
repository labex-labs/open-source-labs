# 제공된 매핑 함수로 배열을 결합하는 함수

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 제공된 매핑 함수를 두 입력 배열의 각 요소에 적용한 후, 두 입력 배열 중 하나에 존재하는 요소의 배열을 반환합니다.

이를 달성하기 위한 단계는 다음과 같습니다.

1. 첫 번째 입력 배열 `a`의 모든 값에 매핑 함수를 적용하여 새로운 `Set`을 생성합니다.
2. 매핑 함수를 적용했을 때 이전에 생성된 `Set`의 값과 일치하지 않는 `b`의 모든 요소로 구성된 다른 `Set`을 생성합니다.
3. 두 세트를 결합하고 배열로 변환합니다.
4. 결과 배열을 반환합니다.

`unionBy` 함수의 코드는 다음과 같습니다.

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

`unionBy` 함수를 사용하는 몇 가지 예는 다음과 같습니다.

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Output: [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Output: [{ id: 1 }, { id: 2 }, { id: 3 }]
```
