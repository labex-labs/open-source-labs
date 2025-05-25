# 음수 0 확인하기

숫자가 음수 0 인지 확인하려면 터미널/SSH 를 열고 `node`를 입력합니다. 그런 다음 다음 코드를 사용합니다.

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

이 코드는 전달된 값이 `0`과 같고 `1`을 값으로 나눈 결과가 `-Infinity`와 같은지 확인합니다. 예를 들어:

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
