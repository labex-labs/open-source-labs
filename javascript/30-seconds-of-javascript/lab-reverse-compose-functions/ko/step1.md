# 함수 합성 뒤집기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 왼쪽에서 오른쪽으로 함수 합성을 수행하는 방법입니다.

- `Array.prototype.reduce()` 메서드를 사용하여 왼쪽에서 오른쪽으로 함수 합성을 수행합니다.
- 첫 번째 (가장 왼쪽) 함수는 하나 이상의 인수를 허용할 수 있지만, 나머지 함수는 단항 (unary) 이어야 합니다.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

예를 들어:

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
