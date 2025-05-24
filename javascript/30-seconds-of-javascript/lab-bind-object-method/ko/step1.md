# 객체 메서드 바인딩 함수

객체 메서드를 해당 컨텍스트에 바인딩하고 선택적으로 추가 매개변수를 앞에 추가하는 함수를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 객체 컨텍스트, 메서드 키 및 앞에 추가할 추가 인수를 받는 함수를 정의합니다.
3. 이 함수는 `Function.prototype.apply()`를 사용하여 메서드를 객체 컨텍스트에 바인딩하는 새로운 함수를 반환해야 합니다.
4. 스프레드 연산자 (`...`) 를 사용하여 제공된 추가 매개변수를 인수에 앞에 추가합니다.
5. 다음은 예시 구현입니다.

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. 함수를 테스트하려면 메서드가 있는 객체를 생성하고 `bindKey()`를 사용하여 바인딩합니다. 그런 다음, 바인딩된 메서드를 일부 인수로 호출합니다.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
