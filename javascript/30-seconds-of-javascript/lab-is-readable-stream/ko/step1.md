# 스트림이 읽기 가능한지 확인하기

주어진 인수가 읽기 가능한 스트림인지 확인하려면 다음 단계를 따르세요.

- 먼저, 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- 값이 `null`이 아닌지 확인합니다.
- `typeof`를 사용하여 값이 `object`이고 `pipe` 속성이 `function`인지 확인합니다.
- 또한, `_read` 및 `_readableState` 속성의 `typeof`가 각각 `function` 및 `object`인지 확인합니다.

다음은 이러한 단계를 구현하는 예시 함수입니다.

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

이 함수를 사용하여 스트림이 읽기 가능한지 확인할 수 있습니다. 예시:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
