# 배열 분할 알고리즘

배열을 분할하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 제공된 함수 `fn`을 주어진 배열 `arr`의 각 값에 적용합니다.
3. `fn`이 새로운 값을 반환할 때마다 배열을 분할합니다.
4. `Array.prototype.reduce()`를 사용하여 결과 배열과 `fn`에서 반환된 마지막 값을 보유하는 누산기 객체를 생성합니다.
5. `Array.prototype.push()`를 사용하여 `arr`의 각 값을 누산기 배열의 적절한 분할에 추가합니다.
6. 결과 배열을 반환합니다.

다음은 코드 구현입니다.

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

사용 예시:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
