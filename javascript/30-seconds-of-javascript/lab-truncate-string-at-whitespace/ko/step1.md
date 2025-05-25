# JavaScript 에서 공백 문자를 기준으로 문자열을 자르는 방법

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 가능한 경우 공백을 존중하면서 지정된 길이까지 문자열을 자르는 함수입니다.

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

이 함수를 사용하려면 자르려는 문자열을 첫 번째 인수로, 최대 길이를 두 번째 인수로, 선택적 ending string(종료 문자열) 을 세 번째 인수로 전달합니다. 문자열의 길이가 지정된 제한보다 작거나 같으면 원래 문자열이 반환됩니다. 그렇지 않으면 함수는 제한 전에 마지막 공백을 찾고 해당 지점에서 문자열을 자른 다음, 지정된 경우 ending string 을 추가합니다.

다음은 몇 가지 예입니다.

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
