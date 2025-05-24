# JavaScript 에서 객체로부터 함수 속성 이름 가져오는 방법

객체에서 함수 속성 이름의 배열을 얻으려면 아래 제공된 `functions` 함수를 사용하십시오. 이 함수는 선택적으로 상속된 속성도 포함할 수 있습니다.

`functions` 함수를 사용하는 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 사용하여 객체의 고유한 속성을 반복합니다.
3. 상속된 속성을 포함하려면 `inherited` 인수를 `true`로 설정하고 `Object.getPrototypeOf()`를 사용하여 객체의 상속된 속성을 가져옵니다.
4. `Array.prototype.filter()`를 사용하여 함수인 속성만 유지합니다.
5. 기본적으로 상속된 속성을 포함하지 않으려면 두 번째 인수 `inherited`를 생략합니다.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

`functions` 함수의 사용 예는 다음과 같습니다.

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
