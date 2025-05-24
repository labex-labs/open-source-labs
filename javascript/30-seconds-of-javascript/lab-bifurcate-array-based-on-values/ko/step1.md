# 배열을 두 그룹으로 분할하는 함수

이 함수를 사용하여 값을 기준으로 배열을 두 그룹으로 분할하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 주어진 `filter` 배열의 결과에 따라 값을 두 그룹으로 분할하는 `bifurcate()` 함수를 사용합니다.
3. 함수를 구현하려면 `Array.prototype.reduce()`와 `Array.prototype.push()`를 사용하여 `filter` 배열을 기반으로 그룹에 요소를 추가합니다.
4. `filter`가 모든 요소에 대해 truthy 값을 가지면 첫 번째 그룹에 추가하고, 그렇지 않으면 두 번째 그룹에 추가합니다.

다음은 `bifurcate()` 함수의 코드입니다.

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

`bifurcate()` 함수를 값의 배열과 해당 필터 배열과 함께 호출하여 값을 두 그룹으로 분할할 수 있습니다. 예를 들어:

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
