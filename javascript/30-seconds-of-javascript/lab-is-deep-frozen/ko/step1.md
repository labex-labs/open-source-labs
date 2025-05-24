# 객체가 깊이 동결되었는지 확인하는 방법

객체가 깊이 동결되었는지 확인하려면 JavaScript 에서 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용하여 객체의 모든 속성이 깊이 동결되었는지 확인합니다.
3. 주어진 객체에 `Object.isFrozen()`을 사용하여 얕게 동결 (shallowly frozen) 되었는지 확인합니다.
4. `Object.keys()`를 사용하여 객체의 모든 속성을 가져오고, `Array.prototype.every()`를 사용하여 모든 키가 깊이 동결된 객체이거나 객체가 아닌 값인지 확인합니다.

다음은 객체가 깊이 동결되었는지 확인하는 코드 스니펫 예시입니다.

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

`isDeepFrozen` 함수를 사용하여 객체가 깊이 동결되었는지 다음과 같이 확인할 수 있습니다.

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
