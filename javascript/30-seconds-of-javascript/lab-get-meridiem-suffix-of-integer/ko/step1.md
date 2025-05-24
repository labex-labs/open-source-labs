# 정수의 자오선 접미사 얻는 방법

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 정수를 자오선 접미사가 있는 12 시간 형식 문자열로 변환하는 함수입니다.

이를 위해 모듈로 연산자 (`%`) 와 조건 검사를 사용합니다.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

이 함수를 사용하는 몇 가지 예는 다음과 같습니다.

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

이 함수는 정수를 인수로 받아 자오선 접미사가 있는 문자열을 반환합니다.
