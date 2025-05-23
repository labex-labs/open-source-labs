# 가변 인자 함수 변환하기

가변 인자 함수를 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. 가변 인자 함수를 받는 함수를 만듭니다.
3. 클로저 (closure) 와 스프레드 연산자 (`...`) 를 사용하여 인자 배열을 함수의 입력에 매핑합니다.
4. 인자 배열을 받아 원래의 가변 인자 함수를 해당 인자로 호출하는 새로운 함수를 반환합니다.

다음은 이 기술을 사용하여 `Math.max` 함수를 변환하는 예시입니다.

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
