# 문자열이 유효한 JSON 인지 확인하기

주어진 문자열이 유효한 JSON 인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `JSON.parse()` 메서드와 `try...catch` 블록을 사용하여 제공된 문자열이 유효한 JSON 인지 확인합니다.
3. 문자열이 유효하면 `true`를 반환합니다. 그렇지 않으면 `false`를 반환합니다.

다음은 이 로직을 구현하는 코드 스니펫 예시입니다.

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

다음과 같이 다양한 입력 문자열로 이 함수를 테스트할 수 있습니다.

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

마지막 예시에서 `null`은 유효한 JSON 문자열이 아니므로 함수는 `false`를 반환합니다.
