# 값이 객체와 유사한지 확인하기

값이 객체와 유사한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. 제공된 값이 `null`이 아니고 `typeof`가 `'object'`와 같은지 확인합니다.

다음은 사용할 수 있는 코드입니다.

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

다음 예제를 사용하여 이 함수를 테스트할 수 있습니다.

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
