# JavaScript 에서 무작위 영숫자 문자열을 생성하는 방법

JavaScript 에서 영숫자 문자의 무작위 문자열을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.from()`을 사용하여 지정된 길이의 새 배열을 생성합니다.
3. `Math.random()`을 사용하여 무작위 부동 소수점 숫자를 생성합니다.
4. `radix` 값이 `36`인 `Number.prototype.toString()`을 사용하여 숫자를 영숫자 문자열로 변환합니다.
5. `String.prototype.slice()`를 사용하여 각 생성된 숫자에서 정수 부분과 소수점을 제거합니다.
6. `Array.prototype.some()`을 사용하여 이 프로세스를 `length`까지 필요한 만큼 반복합니다. `Array.prototype.some()`은 매번 가변 길이 문자열을 생성하기 때문입니다.
7. `String.prototype.slice()`를 사용하여 생성된 문자열이 주어진 `length`보다 길면 잘라냅니다.
8. 생성된 문자열을 반환합니다.

다음은 코드입니다.

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

원하는 길이를 인수로 사용하여 `randomAlphaNumeric()` 함수를 호출할 수 있습니다. 예를 들어:

```js
randomAlphaNumeric(5); // '0afad'
```
