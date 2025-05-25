# 논리적 보수 (Logical Complement)

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

함수 `fn`의 논리적 보수를 얻으려면 `complement` 함수를 사용하십시오. 이 함수는 제공된 모든 인수를 사용하여 `fn`을 호출한 결과에 논리적 not 연산자 (`!`) 를 적용하는 다른 함수를 반환합니다.

다음은 예시 코드 조각입니다.

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

이 함수를 사용하려면, 예를 들어 주어진 숫자가 짝수이면 `true`를 반환하는 `isEven`과 같은 술어 함수 (predicate function) 를 정의하십시오. 그런 다음 아래와 같이 `complement` 함수를 사용하여 이 함수의 논리적 보수를 얻을 수 있습니다.

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
