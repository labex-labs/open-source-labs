# 현재 런타임 환경이 Node.js 인지 확인하는 방법

현재 런타임 환경이 Node.js 인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력합니다.
3. 현재 Node.js 프로세스에 대한 정보를 제공하는 `process` 전역 객체를 사용합니다.
4. `process`, `process.versions`, 그리고 `process.versions.node`가 정의되어 있는지 확인합니다.

현재 런타임 환경이 Node.js 인지 확인하는 코드는 다음과 같습니다.

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

`isNode` 함수를 호출하여 코드를 테스트할 수 있습니다.

```js
isNode(); // true (Node)
isNode(); // false (browser)
```
