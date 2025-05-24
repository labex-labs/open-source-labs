# 배열 내용 동일성 확인

두 배열이 순서에 관계없이 동일한 요소를 포함하는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. 두 배열의 값으로 생성된 `Set`에 대해 `for...of` 루프를 사용합니다.
3. `Array.prototype.filter()`를 사용하여 두 배열에서 각 고유 값의 발생 횟수를 비교합니다.
4. 어떤 요소에 대해서든 횟수가 일치하지 않으면 `false`를 반환하고, 그렇지 않으면 `true`를 반환합니다.

다음은 동일한 기능을 수행하는 코드입니다.

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

함수를 테스트하려면 다음 코드를 사용하세요.

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
