# 배열을 identity object 로 변환하는 방법

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요. 값의 배열을 키와 값으로 동일한 값을 가진 객체로 변환하려면 다음 단계를 따르세요.

1. `Array.prototype.map()`을 사용하여 각 값을 key-value 쌍의 배열로 매핑합니다.
2. `Object.fromEntries()`를 사용하여 key-value 쌍의 배열을 객체로 변환합니다.

다음은 코드입니다.

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

다음은 예시입니다.

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
