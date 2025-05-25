# 값이 일반 객체인지 확인하기

값이 일반 객체인지 확인하려면 다음 단계를 따르세요.

- 값이 truthy 한지 확인합니다.
- `typeof`를 사용하여 객체인지 확인합니다.
- `Object.prototype.constructor`를 사용하여 생성자가 `Object`와 같은지 확인합니다.

이 확인을 구현하려면 다음 코드를 사용하세요.

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

다음 예제를 사용하여 이 함수를 테스트할 수 있습니다.

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.
