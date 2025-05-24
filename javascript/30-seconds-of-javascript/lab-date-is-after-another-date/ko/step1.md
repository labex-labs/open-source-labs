# JavaScript 에서 한 날짜가 다른 날짜보다 뒤인지 확인하는 방법

JavaScript 에서 한 날짜가 다른 날짜보다 뒤에 오는지 확인하려면, 보다 큼 연산자 (`>`) 를 사용할 수 있습니다. 다음은 주어진 날짜 (`dateA`) 가 다른 날짜 (`dateB`) 보다 뒤인지 확인하는 예시 코드 조각입니다.

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

이 함수를 사용하려면 다음과 같이 두 개의 날짜 객체를 전달하면 됩니다.

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

이것을 시도해 보려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작할 수 있습니다.
