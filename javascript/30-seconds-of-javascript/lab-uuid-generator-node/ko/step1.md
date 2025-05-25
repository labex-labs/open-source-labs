# Node.js 에서 UUID 생성하기

Node.js 에서 UUID 를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `crypto.randomBytes()` 메서드를 사용하여 [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) 버전 4 를 준수하는 UUID 를 생성합니다.
3. `Number.prototype.toString()` 메서드를 사용하여 생성된 UUID 를 적절한 UUID(16 진수 문자열) 로 변환합니다.
4. 또는, 유사한 기능을 제공하는 [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) 메서드를 사용할 수 있습니다.

Node.js 에서 UUID 를 생성하는 예시 코드 조각은 다음과 같습니다.

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

`UUIDGeneratorNode()` 메서드를 호출하여 UUID 를 생성할 수 있습니다.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
