# 반복 가능한 객체 청크하기 (Chunk Iterable)

반복 가능한 객체를 지정된 크기의 더 작은 배열로 청크하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 주어진 반복 가능한 객체에 대해 `for...of` 루프를 사용하고, `Array.prototype.push()`를 사용하여 각 새 값을 현재 `chunk`에 추가합니다.
3. `Array.prototype.length`를 사용하여 현재 `chunk`의 크기가 원하는 `size`인지 확인하고, 그렇다면 값을 `yield`합니다.
4. `Array.prototype.length`를 사용하여 마지막 `chunk`를 확인하고, 비어 있지 않은 경우 `yield`합니다.
5. 다음 코드를 사용합니다.

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. 이 코드를 사용하여 함수를 테스트합니다.

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
