# 숫자가 2 의 거듭제곱인지 확인하기

숫자가 2 의 거듭제곱인지 확인하려면 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 비트 단위 AND 연산자 (`&`) 를 사용하여 숫자 (`n`) 가 2 의 거듭제곱인지 확인합니다.
3. 또한, `n`이 falsy 가 아닌지 확인합니다.
4. 다음 코드는 `n`이 2 의 거듭제곱인지 기능적으로 확인합니다:

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

`isPowerOfTwo` 함수를 사용하는 몇 가지 예는 다음과 같습니다:

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
