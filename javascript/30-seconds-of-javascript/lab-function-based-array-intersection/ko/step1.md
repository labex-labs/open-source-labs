# JavaScript 를 사용하여 함수 기반 배열 교집합 찾기

제공된 비교 함수를 기반으로 두 배열 모두에 존재하는 요소를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 제공된 비교자와 함께 `Array.prototype.filter()`와 `Array.prototype.findIndex()`를 사용하여 교차하는 값을 결정합니다.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. 두 배열과 비교 함수를 인수로 사용하여 `intersectionWith()` 함수를 호출합니다.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

이렇게 하면 제공된 비교 함수를 기반으로 두 배열 간의 교차하는 값을 포함하는 배열이 반환됩니다.
