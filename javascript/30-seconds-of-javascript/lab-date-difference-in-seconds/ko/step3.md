# 화살표 함수를 사용하여 날짜 차이 함수 구현하기

이제 날짜 차이를 계산하는 방법을 이해했으므로 화살표 함수를 사용하여 함수를 보다 간결하게 구현해 보겠습니다.

## JavaScript 의 화살표 함수

화살표 함수는 JavaScript 에서 함수를 작성하기 위한 더 짧은 구문을 제공합니다. 화살표 함수 구문을 사용하여 날짜 차이 함수를 다시 작성하는 방법은 다음과 같습니다.

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

이 함수는 이전 함수와 정확히 동일한 작업을 수행하지만 더 깔끔하고 간결한 구문을 사용합니다.

## JavaScript 파일 생성하기

함수를 저장하고 테스트하기 위해 JavaScript 파일을 만들어 보겠습니다. Ctrl+D 를 누르거나 `.exit`를 입력하고 Enter 키를 눌러 Node.js 환경을 종료합니다.

이제 WebIDE 에서 `dateDifference.js`라는 새 파일을 만듭니다.

1. 왼쪽 사이드바에서 "Explorer" 아이콘을 클릭합니다.
2. 파일 탐색기에서 마우스 오른쪽 버튼을 클릭하고 "New File"을 선택합니다.
3. 파일 이름을 `dateDifference.js`로 지정하고 Enter 키를 누릅니다.
4. 다음 코드를 파일에 추가합니다.

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Test examples
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Expected output: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Expected output: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Expected output: 3600
```

Ctrl+S 를 누르거나 File > Save 를 클릭하여 파일을 저장합니다.

## JavaScript 파일 실행하기

방금 만든 파일을 실행하려면 터미널에서 다음 명령을 사용합니다.

```bash
node dateDifference.js
```

다음 출력이 표시되어야 합니다.

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

이는 함수가 올바르게 작동함을 확인합니다.

- 첫 번째 예: 00:00:15 와 00:00:17 의 차이는 2 초입니다.
- 두 번째 예: 00:00:00 과 00:01:00 의 차이는 60 초 (1 분) 입니다.
- 세 번째 예: 00:00:00 과 01:00:00 의 차이는 3600 초 (1 시간) 입니다.
