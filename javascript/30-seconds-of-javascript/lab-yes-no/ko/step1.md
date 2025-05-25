# Yes/No 문자열 확인 함수

문자열이 `'yes'` 또는 `'no'` 응답인지 확인하려면 터미널/SSH 에서 `node`를 입력하여 다음 함수를 사용하십시오.

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- 이 함수는 문자열이 `'y'`/`'yes'`인 경우 `true`를 반환하고, 문자열이 `'n'`/`'no'`인 경우 `false`를 반환합니다.
- 기본 응답을 설정하려면 두 번째 인수 `def`를 생략하십시오. 기본적으로 함수는 `false`를 반환합니다.
- 이 함수는 `RegExp.prototype.test()`를 사용하여 문자열이 `'y'`/`'yes'` 또는 `'n'`/`'no'`와 일치하는지 확인합니다.

사용 예시:

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
