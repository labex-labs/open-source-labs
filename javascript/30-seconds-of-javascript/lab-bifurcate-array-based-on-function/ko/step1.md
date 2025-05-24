# 배열을 두 그룹으로 분할하는 함수

주어진 함수의 결과에 따라 배열을 두 그룹으로 분할하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()` 및 `Array.prototype.push()` 메서드를 사용하여 그룹에 요소를 추가합니다. 이는 각 요소에 대해 주어진 함수 `fn`이 반환하는 값을 기반으로 합니다.
3. `fn`이 모든 요소에 대해 truthy 값을 반환하면 첫 번째 그룹에 추가합니다. 그렇지 않으면 두 번째 그룹에 추가합니다.

다음은 코드입니다.

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

예를 들어, `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`를 호출하면 함수는 `[ ['beep', 'boop', 'bar'], ['foo'] ]`를 반환합니다.
