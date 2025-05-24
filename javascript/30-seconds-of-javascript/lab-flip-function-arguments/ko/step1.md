# Flip 을 사용하여 함수 인수 재정렬

함수 인수의 순서를 바꾸려면 `flip` 함수를 사용하십시오. 이 함수는 함수를 인수로 받아 첫 번째 인수와 마지막 인수를 바꾸는 새로운 함수를 반환합니다.

`flip`을 구현하려면 다음을 수행하십시오.

- 인수 분해 (argument destructuring) 와 가변 인자 (variadic arguments) 를 사용하는 클로저 (closure) 를 사용합니다.
- 나머지 인수를 적용하기 전에 스프레드 연산자 (`...`) 를 사용하여 첫 번째 인수를 마지막 인수로 만듭니다.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

`flip`을 사용하여 `Object.assign`의 인수를 재정렬하는 방법의 예는 다음과 같습니다.

```js
let a = { name: "John Smith" };
let b = {};

// Object.assign 의 인수를 바꾸는 새로운 함수 생성
const mergeFrom = flip(Object.assign);

// 첫 번째 인수를 a 에 바인딩하는 새로운 함수 생성
let mergePerson = mergeFrom.bind(null, a);

// b 를 두 번째 인수로 사용하여 새 함수 호출
mergePerson(b); // b is now equal to a

// 또는, 새 함수를 사용하지 않고 a 와 b 병합
b = {};
Object.assign(b, a); // b is now equal to a
```
