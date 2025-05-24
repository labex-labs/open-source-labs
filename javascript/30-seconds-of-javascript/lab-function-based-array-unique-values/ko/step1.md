# 함수를 사용하여 배열에서 고유 값 찾기

배열의 모든 고유 값을 찾으려면 비교 함수를 제공하십시오.

`Array.prototype.reduce()` 및 `Array.prototype.some()`을 사용하여 각 값의 첫 번째 고유 발생만 포함하는 배열을 생성합니다. 비교 함수 `fn`은 비교되는 두 요소의 값을 인수로 받습니다.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

함수를 테스트하려면 아래 예제를 사용하십시오.

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Terminal/SSH를 열고 `node`를 입력하여 코딩 연습을 시작하십시오.
