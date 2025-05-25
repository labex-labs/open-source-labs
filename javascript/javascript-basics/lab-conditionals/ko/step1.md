# 조건문 (Conditionals)

> 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하세요.

조건문은 표현식의 결과가 참인지 여부를 테스트하는 데 사용되는 코드 구조입니다. 조건문의 매우 일반적인 형태는 `if...else` 문입니다. 예를 들어 다음과 같습니다.

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

`if ()` 안의 표현식은 테스트입니다. 이 표현식은 변수 `iceCream`과 문자열 `chocolate`을 비교하여 두 값이 같은지 확인하기 위해 엄격한 동등 연산자 (strict equality operator, 위에서 설명) 를 사용합니다. 이 비교가 `true`를 반환하면 첫 번째 코드 블록이 실행됩니다. 비교가 참이 아니면 `else` 문 뒤의 두 번째 코드 블록이 대신 실행됩니다.
