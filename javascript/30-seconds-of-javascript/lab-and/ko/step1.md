# 논리 AND 연산자 사용하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 그런 다음 논리 AND (`&&`) 연산자를 사용하여 두 인수가 모두 `true`인지 확인합니다. 다음은 예시 코드입니다.

```js
const and = (a, b) => a && b;
and(true, true); // true
and(true, false); // false
and(false, false); // false
```
