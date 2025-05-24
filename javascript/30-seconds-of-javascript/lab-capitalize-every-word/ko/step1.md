# JavaScript 에서 각 단어의 첫 글자를 대문자로 만드는 방법

JavaScript 를 사용하여 문자열의 각 단어의 첫 글자를 대문자로 만들려면 `String.prototype.replace()` 메서드를 사용하여 각 단어의 첫 번째 문자를 일치시키고, `String.prototype.toUpperCase()` 메서드를 사용하여 대문자로 변환할 수 있습니다.

다음은 사용할 수 있는 코드 스니펫 예시입니다.

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

이 함수를 사용하려면 대문자로 변환하려는 문자열을 다음과 같이 인수로 전달합니다.

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

이렇게 하면 대문자로 변환된 문자열 'Hello World!'가 반환됩니다.
