# 부분 적용을 사용하여 함수 인수 앞에 추가하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

`partial` 함수는 `fn`을 `partials`를 첫 번째 인수로 호출하는 새로운 함수를 생성하는 데 사용됩니다.

- 스프레드 연산자 (`...`) 를 사용하여 `partials`를 `fn`의 인수 목록 앞에 추가합니다.

```js
const partial =
  (fn, ...partials) =>
  (...args) =>
    fn(...partials, ...args);
```

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetHello = partial(greet, "Hello");
greetHello("John"); // 'Hello John!'
```
