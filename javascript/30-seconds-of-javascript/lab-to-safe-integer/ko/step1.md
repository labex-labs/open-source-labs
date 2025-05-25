# 값을 안전한 정수로 변환하기

값을 안전한 정수로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.max()`와 `Math.min()`을 사용하여 가장 가까운 안전한 값을 찾습니다.
3. `Math.round()`를 사용하여 값을 정수로 변환합니다.

다음은 값을 안전한 정수로 변환하는 방법을 보여주는 코드 예시입니다.

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

다음 입력을 사용하여 이 함수를 테스트할 수 있습니다.

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
