# 해밍 거리 계산

두 값 사이의 해밍 거리를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. XOR 연산자 (`^`) 를 사용하여 두 숫자 간의 비트 차이를 찾습니다.
3. `Number.prototype.toString()`을 사용하여 결과를 이진 문자열로 변환합니다.
4. `String.prototype.match()`를 사용하여 문자열에서 `1`의 개수를 셉니다.
5. 개수를 반환합니다.

다음은 `hammingDistance` 함수의 코드입니다.

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

`hammingDistance(2, 3); // 1`을 실행하여 함수를 테스트할 수 있습니다.
