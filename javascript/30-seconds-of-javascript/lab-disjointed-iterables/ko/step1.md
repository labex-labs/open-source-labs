# 서로소 (Disjointed) 반복 가능 객체 확인하기

두 개의 반복 가능 객체가 공통 값을 가지지 않는지 확인하려면 `isDisjoint` 함수를 사용할 수 있습니다.

사용 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Set` 생성자를 사용하여 각 반복 가능 객체로부터 새로운 `Set` 객체를 생성합니다.
3. `Array.prototype.every()`와 `Set.prototype.has()`를 사용하여 두 반복 가능 객체가 공통 값을 가지지 않는지 확인합니다.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

다음은 몇 가지 예시입니다.

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
