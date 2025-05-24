# 코딩 및 공통 키 찾기 팁

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요.

두 객체 간의 공통 키를 찾으려면 다음 단계를 따르세요.

1. `Object.keys()`를 사용하여 첫 번째 객체의 키를 가져옵니다.
2. `Object.prototype.hasOwnProperty()`를 사용하여 두 번째 객체에 첫 번째 객체에 있는 키가 있는지 확인합니다.
3. `Array.prototype.filter()`를 사용하여 두 객체 모두에 없는 키를 필터링합니다.

다음은 코드의 예입니다.

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

다음 예제로 코드를 테스트할 수 있습니다.

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
