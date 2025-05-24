# 숫자 서식 지정 함수

로컬 숫자 형식 순서를 사용하여 숫자를 서식 지정하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Number.prototype.toLocaleString()` 메서드를 사용하여 숫자를 로컬 숫자 형식 구분 기호를 사용하여 변환합니다.
3. 서식 지정하려는 숫자를 함수의 인수로 전달합니다.

다음은 예시 구현입니다.

```js
const formatNumber = (num) => num.toLocaleString();
```

다음은 함수 사용 예시입니다.

```js
formatNumber(123456); // '123,456' in `en-US`
formatNumber(15675436903); // '15.675.436.903' in `de-DE`
```
