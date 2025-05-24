# 주어진 컨텍스트를 가진 함수 생성하기

주어진 컨텍스트를 가진 함수를 생성하려면 `bind` 함수를 사용합니다. 먼저 터미널/SSH 를 열고 `node`를 입력합니다.

`bind` 함수는 주어진 컨텍스트로 원래 함수를 호출하는 새로운 함수를 생성합니다. 또한 선택적으로 제공된 추가 매개변수를 인수에 추가할 수도 있습니다.

`bind`를 사용하려면 원래 함수 (`fn`) 와 원하는 컨텍스트 (`context`) 를 전달합니다. 또한 함수에 바인딩되어야 하는 추가 매개변수 (`...boundArgs`) 를 전달할 수도 있습니다.

`bind` 함수는 `Function.prototype.apply()`를 사용하여 주어진 `context`를 `fn`에 적용하는 새로운 함수를 반환합니다. 또한 스프레드 연산자 (`...`) 를 사용하여 제공된 추가 매개변수를 인수에 추가합니다.

다음은 `bind`의 사용 예시입니다.

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

이 예제에서는 두 개의 매개변수 (`greeting` 및 `punctuation`) 를 받아 `greeting`, 현재 컨텍스트 (`this`) 의 `user` 속성, 그리고 `punctuation`을 연결한 문자열을 반환하는 `greet` 함수를 정의합니다.

그런 다음 `user` 속성이 `'fred'`로 설정된 새로운 객체 (`freddy`) 를 생성합니다.

마지막으로, `greet` 함수와 원하는 컨텍스트로 `freddy` 객체를 전달하여 `bind`를 사용하여 새로운 함수 (`freddyBound`) 를 생성합니다. 그런 다음 `freddyBound`를 두 개의 추가 매개변수 (`'hi'` 및 `'!'`) 로 호출할 수 있으며, 이는 바인딩된 `freddy` 컨텍스트와 함께 원래 `greet` 함수로 전달됩니다. 결과 출력은 `'hi fred!'`입니다.
