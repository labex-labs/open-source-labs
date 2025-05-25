# JavaScript 에서 문자열이 회문 (Palindrome) 인지 확인하는 방법?

JavaScript 에서 주어진 문자열이 회문인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.toLowerCase()` 메서드를 사용하여 문자열을 소문자로 정규화합니다.
3. `String.prototype.replace()` 메서드와 정규 표현식 `[\W_]`를 사용하여 문자열에서 영숫자가 아닌 문자를 제거합니다.
4. 스프레드 연산자 (`...`) 를 사용하여 정규화된 문자열을 개별 문자로 분할합니다.
5. `Array.prototype.reverse()` 메서드를 사용하여 문자 배열을 뒤집습니다.
6. `Array.prototype.join()` 메서드를 사용하여 뒤집힌 문자 배열을 문자열로 결합합니다.
7. 뒤집힌 문자열을 정규화된 문자열과 비교하여 회문인지 확인합니다.

위 단계를 구현하는 예시 코드 조각은 다음과 같습니다.

```js
const palindrome = (str) => {
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, "");
  return normalizedStr === [...normalizedStr].reverse().join("");
};

console.log(palindrome("taco cat")); // true
```

위 예제에서 `palindrome()` 함수는 문자열 인수를 받아 문자열이 회문이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다. 이 함수는 문자열이 회문인지 확인하기 위해 위에 설명된 단계를 사용합니다.
