# JavaScript 에서 날짜 계산 이해하기

이제 Date 객체를 생성하는 방법을 이해했으므로 두 날짜 간의 차이를 계산하는 방법을 배워보겠습니다.

## JavaScript 에서의 날짜 산술 연산

JavaScript 를 사용하면 Date 객체에 직접 산술 연산을 수행할 수 있습니다. 한 Date 객체에서 다른 Date 객체를 빼면 JavaScript 는 자동으로 이를 타임스탬프 (밀리초) 로 변환하고 뺄셈을 수행합니다.

```javascript
let date1 = new Date("2023-01-01T00:00:00");
let date2 = new Date("2023-01-01T00:01:00");

let differenceInMilliseconds = date2 - date1;
console.log(differenceInMilliseconds); // 60000 (60 seconds * 1000 milliseconds)
```

Node.js 환경에서 이 코드를 실행해 보세요. 결과는 `60000`이어야 하며, 이는 60 초를 밀리초로 나타냅니다.

## 밀리초를 초로 변환하기

시간 차이를 밀리초에서 초로 변환하려면 1000 으로 나누면 됩니다.

```javascript
let differenceInSeconds = differenceInMilliseconds / 1000;
console.log(differenceInSeconds); // 60
```

이 예제에서는 시간 차이가 초 단위로 60 초, 즉 1 분이 됩니다.

## 날짜 차이 함수 생성하기

이제 개념을 이해했으므로 두 날짜 간의 차이를 초 단위로 계산하는 간단한 함수를 만들어 보겠습니다.

```javascript
function getDateDifferenceInSeconds(startDate, endDate) {
  return (endDate - startDate) / 1000;
}

// Test the function
let start = new Date("2023-01-01T00:00:00");
let end = new Date("2023-01-01T00:01:30");
let difference = getDateDifferenceInSeconds(start, end);
console.log(difference); // 90 (1 minute and 30 seconds)
```

Node.js 환경에서 이 함수를 입력하고 실행해 보세요. 결과는 `90`이어야 하며, 이는 1 분 30 초를 나타냅니다.
