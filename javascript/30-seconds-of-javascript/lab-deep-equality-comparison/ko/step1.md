# JavaScript 에서 객체 동일성 확인 방법

두 값이 동일한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `equals()` 함수를 사용하여 두 값 간의 심층 비교 (deep comparison) 를 수행합니다.
3. 두 값이 동일한지 확인합니다. 그렇다면 `true`를 반환합니다.
4. `Date.prototype.getTime()`을 사용하여 두 값이 동일한 시간을 가진 `Date` 객체인지 확인합니다. 그렇다면 `true`를 반환합니다.
5. 두 값이 동일한 값을 가진 비 객체 값 (strict comparison) 인지 확인합니다. 그렇다면 `true`를 반환합니다.
6. 값 중 하나만 `null` 또는 `undefined`이거나 프로토타입이 다른지 확인합니다. 그렇다면 `false`를 반환합니다.
7. 위의 조건 중 어느 것도 충족되지 않으면 `Object.keys()`를 사용하여 두 값 모두 동일한 수의 키를 가지고 있는지 확인합니다.
8. `Array.prototype.every()`를 사용하여 `a`의 모든 키가 `b`에 존재하고 `equals()`를 재귀적으로 호출하여 동일한지 확인합니다.

`equals()` 함수를 구현하려면 다음 코드를 사용하세요.

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

`equals()` 함수를 테스트하려면 다음 코드 예제를 사용하세요.

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
