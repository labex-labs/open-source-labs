# JavaScript 에서 함수 실행 지연 방법

JavaScript 에서 함수의 실행을 지연시키려면 `setTimeout()` 메서드를 사용할 수 있습니다. 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 구문을 사용하여 함수 `fn`의 실행을 `ms` 밀리초 (milliseconds) 만큼 지연시킵니다.

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. 함수에 인수를 전달하려면 스프레드 연산자 (`...`) 를 다음과 같이 사용합니다.

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // Logs 'later' after one second.
```

이 코드를 사용하면 제공된 함수 `fn`이 지정된 밀리초 수 (`ms`) 후에 호출됩니다. `...args` 매개변수를 사용하면 함수에 임의의 수의 인수를 전달할 수 있습니다.
