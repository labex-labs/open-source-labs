# JavaScript 에서 무작위 부울 값 생성 방법

JavaScript 에서 무작위 부울 값을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.random()` 메서드를 사용하여 무작위 숫자를 생성합니다.
3. 무작위 숫자가 `0.5` 이상인지 확인합니다.
4. 숫자가 `0.5` 이상이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 코드의 간결한 구현입니다.

```js
const randomBoolean = () => Math.random() >= 0.5;
```

`randomBoolean()`을 호출하여 함수를 테스트할 수 있으며, 이 함수는 `true` 또는 `false`를 반환합니다.
