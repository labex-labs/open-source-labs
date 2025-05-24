# 지정된 값으로 배열을 초기화하는 함수

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

이 함수는 지정된 값으로 배열을 초기화합니다.

- `Array()` 생성자를 사용하여 원하는 길이의 배열을 생성합니다.
- `Array.prototype.fill()`을 사용하여 원하는 값으로 채웁니다.
- 값이 지정되지 않으면 기본값은 `0`입니다.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

사용 예시:

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
