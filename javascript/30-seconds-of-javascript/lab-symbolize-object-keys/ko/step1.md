# JavaScript 에서 객체 키를 심볼화하는 방법

JavaScript 에서 객체 키를 심볼화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()` 메서드를 사용하여 심볼화하려는 객체의 키를 가져옵니다.
3. `Array.prototype.reduce()` 메서드와 `Symbol`을 사용하여 각 키가 `Symbol`로 변환된 새로운 객체를 생성합니다.
4. 다음은 예시 코드 조각입니다.

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. 함수를 테스트하려면 다음과 같이 객체를 인수로 사용하여 `symbolizeKeys()`를 호출합니다.

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

이러한 단계를 따르면 JavaScript 에서 모든 객체의 키를 쉽게 심볼화할 수 있습니다.
