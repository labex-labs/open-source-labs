# 배열의 연속된 요소 매핑 함수

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

이 함수는 주어진 함수 `fn`을 사용하여 배열의 각 `n`개의 연속된 요소 블록을 매핑합니다. 다음 단계를 따르십시오.

- `Array.prototype.slice()`를 사용하여 처음 `n`개의 요소가 제거된 새 배열 `arr`을 얻습니다.
- `Array.prototype.map()` 및 `Array.prototype.slice()`를 사용하여 `arr`의 각 `n`개의 연속된 요소 블록에 `fn`을 적용합니다.

다음은 코드입니다.

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

예를 들어, `mapConsecutive()`를 사용하여 숫자 배열에서 3 개의 연속된 각 요소 블록을 매핑하고 대시로 연결할 수 있습니다.

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
