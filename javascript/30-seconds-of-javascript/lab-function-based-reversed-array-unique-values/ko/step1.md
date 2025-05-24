# 배열에서 역순 고유 값 찾기 함수

제공된 비교 함수를 기반으로 배열의 모든 고유 값을 오른쪽에서 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduceRight()` 및 `Array.prototype.some()`을 사용하여 비교 함수 `fn`을 기반으로 각 값의 마지막 고유 발생만 포함하는 배열을 만듭니다.
3. 비교 함수는 두 개의 인수를 받습니다: 비교되는 두 요소의 값입니다.
4. 다음은 함수를 구현하는 코드입니다.

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. 다음 코드를 사용하여 함수를 테스트합니다.

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
