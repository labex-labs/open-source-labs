# JavaScript 에서 객체를 딥 프리즈하는 방법

JavaScript 에서 객체를 딥 프리즈하려면 다음 단계를 따르세요.

1. `Object.keys()`를 사용하여 전달된 객체의 모든 속성을 가져옵니다.
2. `Array.prototype.forEach()`를 사용하여 속성을 반복합니다.
3. 객체인 모든 속성에 대해 `Object.freeze()`를 재귀적으로 호출하여 필요에 따라 `deepFreeze()`를 적용합니다.
4. 마지막으로 `Object.freeze()`를 사용하여 주어진 객체를 프리즈합니다.

다음은 코드입니다.

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

다음 코드를 사용하여 딥 프리즈된 객체를 테스트할 수 있습니다.

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // not allowed
val[1][0] = 4; // not allowed as well
```

위 코드는 `val` 객체가 딥 프리즈되어 수정할 수 없기 때문에 오류를 발생시킵니다.
