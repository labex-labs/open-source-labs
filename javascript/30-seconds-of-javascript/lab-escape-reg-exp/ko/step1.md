# JavaScript 에서 정규 표현식 이스케이프 방법

JavaScript 에서 정규 표현식에 사용할 문자열을 이스케이프하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.replace()`를 사용하여 특수 문자를 이스케이프합니다.
3. 다음 코드 스니펫을 복사하여 붙여넣습니다.

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. `escapeRegExp()` 함수를 사용하여 문자열 내 특수 문자를 이스케이프합니다.

다음은 예시입니다.

```js
escapeRegExp("(test)"); // \\(test\\)
```

이러한 단계를 통해 JavaScript 에서 정규 표현식의 모든 특수 문자를 쉽게 이스케이프할 수 있습니다.
