# JavaScript 에서 정렬된 배열 병합하기 위한 지침

JavaScript 에서 정렬된 두 개의 배열을 병합하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 스프레드 연산자 (`...`) 를 사용하여 주어진 두 배열을 복제합니다.
3. `Array.from()`을 사용하여 주어진 배열을 기반으로 적절한 길이의 배열을 생성합니다.
4. `Array.prototype.shift()`를 사용하여 복제된 배열에서 제거된 요소로 새로 생성된 배열을 채웁니다.

다음은 정렬된 두 배열을 병합하는 예시 코드 조각입니다.

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // Output: [1, 2, 3, 4, 5, 6]
```

위 코드에서 `mergeSortedArrays` 함수는 두 개의 정렬된 배열을 인수로 받아 위 단계를 따라 병합된 배열을 반환합니다. 예시 코드의 출력은 `[1, 2, 3, 4, 5, 6]`입니다.
