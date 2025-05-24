# JavaScript 로 배열을 평탄화하는 방법

JavaScript 에서 지정된 깊이까지 배열을 평탄화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `flatten` 함수를 두 개의 인자, 즉 `arr` (평탄화할 배열) 과 `depth` (평탄화할 중첩 레벨의 최대 수) 와 함께 사용합니다.
3. `flatten` 함수 내부에서 재귀 (recursion) 를 사용하여 각 깊이 레벨마다 `depth`를 `1`씩 감소시킵니다.
4. `Array.prototype.reduce()`와 `Array.prototype.concat()`을 사용하여 요소 또는 배열을 병합합니다.
5. `depth`가 `1`과 같을 때 재귀를 중단하기 위한 기본 사례 (base case) 를 추가합니다.
6. 두 번째 인자 `depth`를 생략하여 깊이 `1`까지만 평탄화합니다 (단일 평탄화).

다음은 `flatten` 함수의 코드입니다.

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

다음 예제를 사용하여 `flatten` 함수를 테스트할 수 있습니다.

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
