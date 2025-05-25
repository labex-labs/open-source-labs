# 객체 변환

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

`transform` 함수는 누산기 (accumulator) 와 객체의 각 키에 대해 지정된 함수를 왼쪽에서 오른쪽으로 적용합니다. 사용 방법은 다음과 같습니다.

- `Object.keys()`를 사용하여 객체의 각 키를 반복합니다.
- `Array.prototype.reduce()`를 사용하여 지정된 함수를 주어진 누산기에 적용합니다.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

다음은 예시입니다.

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
