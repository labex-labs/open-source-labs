# 인수를 추가하는 함수

인수를 받는 인수에 인수를 추가하는 함수를 만들려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 스프레드 연산자 (`...`) 를 사용하여 `partials`를 `fn`의 인수 목록에 추가합니다.
3. 다음 코드를 사용하여 함수를 만듭니다.

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. 다음 예시와 같이 함수를 테스트합니다.

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
