# 문자열 패딩 함수

지정된 문자를 사용하여 문자열의 양쪽을 패딩하고, 문자열의 길이가 지정된 `length`보다 짧은 경우, 다음 함수를 사용합니다.

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

이 함수는 `String.prototype.padStart()` 및 `String.prototype.padEnd()`를 사용하여 주어진 문자열의 양쪽을 패딩합니다. 세 번째 인자 `char`를 생략하면 공백 문자를 기본 패딩 문자로 사용할 수 있습니다.

다음은 `pad()` 함수를 사용하는 몇 가지 예시입니다.

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.
