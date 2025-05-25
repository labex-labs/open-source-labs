# 스트림이 듀플렉스인지 확인하기

스트림이 듀플렉스 (duplex, 읽기 및 쓰기 가능) 인지 확인하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다. 그런 다음 다음 단계를 따르세요.

1. 주어진 인수가 `null`과 다른지 확인합니다.
2. `typeof`를 사용하여 주어진 인수가 `object` 유형인지, 그리고 `function` 유형의 `pipe` 속성을 가지고 있는지 확인합니다.
3. 또한, `_read`, `_write`, `_readableState`, 및 `_writableState` 속성이 각각 `function` 및 `object` 유형인지 확인합니다.

다음은 코드입니다.

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

다음 예제를 사용하여 이 코드를 테스트할 수 있습니다.

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
