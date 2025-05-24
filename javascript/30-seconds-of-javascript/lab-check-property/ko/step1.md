# 속성 검사기

객체의 특정 속성이 특정 조건을 충족하는지 확인하려면 `checkProp` 함수를 사용하십시오. 이 함수는 술어 함수 (predicate function) 와 속성 이름을 인수로 사용하는 커링된 (curried) 함수를 생성합니다. 그런 다음 반환된 함수는 객체를 인수로 받아 지정된 속성이 술어 함수에 의해 지정된 조건을 충족하는지 여부에 따라 `true` 또는 `false`를 반환합니다.

다음은 `checkProp`의 예시 구현입니다.

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

다음은 이 함수를 사용하는 몇 가지 예시입니다.

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set uses Size, not length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

요약하면, `checkProp` 함수를 사용하면 해당 속성에 대한 술어 함수를 지정하여 객체의 특정 속성 값을 쉽게 확인할 수 있습니다.
