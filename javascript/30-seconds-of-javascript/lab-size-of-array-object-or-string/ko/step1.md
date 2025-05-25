# 배열, 객체 또는 문자열의 크기를 구하는 함수

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이 함수는 배열, 객체 또는 문자열의 크기를 구합니다.

사용 방법:

- `val`의 유형을 결정합니다 (`array`, `object` 또는 `string`).
- 배열의 경우 `Array.prototype.length` 속성을 사용합니다.
- 사용 가능한 경우 `length` 또는 `size` 값을 사용하거나, 객체의 경우 키의 수를 사용합니다.
- 문자열의 경우 `val`에서 생성된 [`Blob` 객체](https://developer.mozilla.org/en-US/docs/Web/API/Blob)의 `size`를 사용합니다.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

예시:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
