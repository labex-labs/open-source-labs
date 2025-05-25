# 진실 확인 컬렉션 함수

코딩 연습을 위해 터미널/SSH 에서 `node`를 입력하세요.

다음은 컬렉션의 모든 요소에 대해 술어 함수가 참인지 확인하는 함수입니다.

- `Array.prototype.every()`를 사용하여 각 전달된 객체가 지정된 속성을 가지고 있는지, 그리고 참 같은 값을 반환하는지 확인합니다.

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

사용 예시:

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
