# JavaScript 에서 문자열을 문자 배열로 변환하는 방법

JavaScript 에서 문자열을 문자 배열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. Spread operator (전개 연산자) (`...`) 를 사용하여 문자열을 문자 배열로 변환합니다.
3. 문자열을 인수로 받아 해당 문자의 배열을 반환하는 `toCharArray`라는 함수를 정의합니다.
4. 변환하려는 문자열을 인수로 사용하여 `toCharArray` 함수를 호출합니다.
5. 함수는 문자 배열을 반환합니다.

다음은 코드입니다.

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
