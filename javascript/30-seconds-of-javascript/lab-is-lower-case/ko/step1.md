# 문자열이 소문자인지 확인하는 JavaScript 함수

주어진 문자열이 소문자인지 확인하려면 다음 JavaScript 함수를 사용할 수 있습니다. 먼저, `String.prototype.toLowerCase()`를 사용하여 문자열을 소문자로 변환한 다음, 엄격한 동일성 연산자 (`===`) 를 사용하여 원래 문자열과 비교합니다.

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

다음은 사용 예시입니다.

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
