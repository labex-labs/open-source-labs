# 문자열 내 공백 확인

문자열에 공백 문자가 포함되어 있는지 확인하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `RegExp.prototype.test()`를 적절한 정규 표현식 (regular expression) 과 함께 사용하여 주어진 문자열에 공백 문자가 포함되어 있는지 확인합니다.
- 다음은 예시 코드 조각입니다.

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- 함수를 테스트하려면 문자열을 인수로 사용하여 `containsWhitespace`를 호출합니다. 문자열에 공백 문자가 포함되어 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
