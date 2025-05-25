# 함수 인수 변환

함수 인수를 변환하려면 `overArgs` 함수를 사용하십시오. 이 함수는 제공된 함수를 변환된 인수로 호출하는 새로운 함수를 생성합니다.

- 인수를 변환하려면 `Array.prototype.map()`을 스프레드 연산자 (`...`) 와 함께 사용하고 변환된 인수를 `fn`에 전달합니다.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- `overArgs` 함수를 테스트하려면 샘플 함수와 변환 배열을 생성한 다음, 새로운 함수를 인수로 호출합니다.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
