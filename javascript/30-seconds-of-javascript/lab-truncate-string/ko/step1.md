# JavaScript 에서 문자열 자르기 (Truncate a String)

JavaScript 에서 문자열을 자르기 (truncate) 위해 `truncateString` 함수를 사용할 수 있습니다. 이 함수는 두 개의 인수를 받습니다: `str` (자르기할 문자열) 과 `num` (자른 문자열의 최대 길이).

`truncateString` 함수는 `str`의 길이가 `num`보다 큰지 확인합니다. 만약 그렇다면, 함수는 문자열을 원하는 길이로 자르고 끝에 `'...'`을 추가합니다. 그렇지 않으면, 원래 문자열을 반환합니다.

다음은 `truncateString` 함수의 코드입니다:

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

다음은 `truncateString` 함수를 사용하는 예시입니다:

```js
truncateString("boomerang", 7); // 'boom...'
```
