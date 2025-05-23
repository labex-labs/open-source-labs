# 특정 크기의 청크로 배열 분할하는 방법

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요.

배열을 지정된 크기의 더 작은 배열로 분할하려면 다음 단계를 따르세요.

1. `Array.from()`을 사용하여 생성될 청크의 수에 맞는 새 배열을 생성합니다.
2. `Array.prototype.slice()`를 사용하여 새 배열의 각 요소를 `size` 길이의 청크에 매핑합니다.
3. 원래 배열을 균등하게 분할할 수 없는 경우, 마지막 청크에는 나머지 요소가 포함됩니다.

다음은 예시 코드 조각입니다.

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

분할하려는 배열과 청크의 원하는 크기를 전달하여 이 함수를 사용할 수 있습니다. 예를 들어:

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
