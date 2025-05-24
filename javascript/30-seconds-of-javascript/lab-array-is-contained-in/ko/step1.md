# 한 배열이 다른 배열에 포함되어 있는지 확인하는 함수

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 이 함수는 첫 번째 배열의 모든 요소가 순서에 관계없이 두 번째 배열에 존재하는지 확인합니다.

다음은 따라야 할 단계입니다.

1. 첫 번째 배열에서 생성된 `Set`을 반복하기 위해 `for...of` 루프를 사용합니다.
2. 모든 고유한 값이 두 번째 배열에 있는지 확인하기 위해 `Array.prototype.some()`을 적용합니다.
3. 두 배열에서 각 고유 값의 발생 횟수를 비교하기 위해 `Array.prototype.filter()`를 사용합니다.
4. 첫 번째 배열에서 어떤 요소의 개수가 두 번째 배열보다 크면 `false`를 반환합니다. 그렇지 않으면 `true`를 반환합니다.

작동 방식을 보려면 아래 코드를 확인하세요.

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

함수를 테스트하려면 다음 코드를 사용하세요.

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
