# 스트림 (Stream) 이 쓰기 가능한지 확인하기

스트림이 쓰기 가능한지 확인하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다. 그런 다음 다음 단계를 따르세요.

1. 주어진 인수가 `null`이 아닌지 확인합니다.
2. `typeof`를 사용하여 값이 `object`인지, 그리고 `pipe` 속성이 `function`인지 확인합니다.
3. 또한, `_write` 및 `_writableState` 속성의 `typeof`가 각각 `function` 및 `object`인지 확인합니다.

다음은 이러한 검사를 구현하는 예제 코드입니다.

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Node.js 의 `fs` 모듈을 사용하여 이 함수를 테스트할 수 있습니다. 예를 들어:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
