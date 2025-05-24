# 문자열이 절대 URL 인지 확인하는 함수

주어진 문자열이 절대 URL 인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `RegExp.prototype.test()`를 사용하여 문자열이 절대 URL 인지 테스트합니다.
3. 함수는 `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`로 정의되어야 합니다.
4. 이 함수는 문자열 인자 `str`을 받아서 문자열이 절대 URL 이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
5. 제공된 예제를 사용하여 함수를 테스트합니다.

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
