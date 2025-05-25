# 문자열을 단어 배열로 변환하는 함수

주어진 문자열을 단어 배열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.split()` 메서드를 제공된 `pattern` (기본값은 알파벳이 아닌 정규 표현식) 과 함께 사용하여 문자열 배열로 변환합니다.
3. `Array.prototype.filter()` 메서드를 사용하여 빈 문자열을 제거합니다.
4. 두 번째 인수 `pattern`을 생략하여 기본 정규 표현식을 사용합니다.

다음은 이러한 단계를 구현하는 함수입니다.

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

`words()` 함수를 사용하여 다양한 문자열을 단어 배열로 변환할 수 있습니다.

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
