# 프로세스 인수에 플래그가 포함되어 있는지 확인

현재 프로세스의 인수에 지정된 플래그가 포함되어 있는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.every()` 및 `Array.prototype.includes()`를 사용하여 `process.argv`에 지정된 모든 플래그가 포함되어 있는지 확인합니다.
3. 정규 표현식 (regular expression) 을 사용하여 지정된 플래그에 `-` 또는 `--`가 접두사로 붙어 있는지 테스트하고, 그에 따라 접두사를 붙입니다.

다음은 이를 구현하는 방법을 보여주는 코드 조각입니다.

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

다음과 같이 다양한 플래그로 함수를 테스트할 수 있습니다.

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
