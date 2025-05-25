# Node.js 에서 값이 스트림인지 확인하는 방법

Node.js 에서 값이 스트림인지 확인하려면 `isStream` 함수를 사용할 수 있습니다. 이 함수를 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. `isStream` 함수를 사용하여 주어진 인수가 스트림인지 확인합니다.
4. 값이 `null`과 다른지 확인하려면 다음 코드를 사용합니다.

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. 파일이 스트림인지 확인하려면 다음 코드를 사용합니다.

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
