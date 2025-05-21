# 실용적인 애플리케이션 만들기

이제 날짜 간의 차이를 초 단위로 계산하는 작동하는 함수가 있으므로, 보다 실용적인 애플리케이션을 만들어 보겠습니다. 시작한 이후로 얼마나 많은 시간이 지났는지 계산하는 간단한 타이머를 만들 것입니다.

## 타이머 애플리케이션 만들기

WebIDE 에서 `timer.js`라는 새 파일을 만듭니다.

1. 왼쪽 사이드바에서 "Explorer" 아이콘을 클릭합니다.
2. 파일 탐색기에서 마우스 오른쪽 버튼을 클릭하고 "New File"을 선택합니다.
3. 파일 이름을 `timer.js`로 지정하고 Enter 키를 누릅니다.
4. 다음 코드를 파일에 추가합니다.

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Start time - when the script starts running
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Function to update and display the elapsed time
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Format the time as hours:minutes:seconds
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Clear the console and display the updated time
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Update the timer every second
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Keep the script running
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Run for 1 minute
```

Ctrl+S 를 누르거나 File > Save 를 클릭하여 파일을 저장합니다.

## 타이머 애플리케이션 실행하기

타이머 애플리케이션을 실행하려면 터미널에서 다음 명령을 사용합니다.

```bash
node timer.js
```

타이머가 시작되어 시작된 이후로 얼마나 많은 시간이 지났는지 매초 업데이트됩니다. 타이머는 1 분 후에 자동으로 중지되거나, Ctrl+C 를 눌러 더 일찍 중지할 수 있습니다.

## 타이머 애플리케이션 이해하기

타이머 애플리케이션이 어떻게 작동하는지 자세히 살펴보겠습니다.

1. 초 단위로 시간 차이를 계산하기 위해 `getSecondsDiffBetweenDates` 함수를 정의합니다.
2. 스크립트가 실행을 시작할 때 시작 시간을 기록합니다.
3. 다음을 수행하는 `updateTimer` 함수를 정의합니다.
   - 현재 시간을 가져옵니다.
   - 시작 시간 이후 경과된 시간을 초 단위로 계산합니다.
   - 경과된 시간을 시:분:초 형식으로 지정합니다.
   - 형식화된 시간을 표시합니다.
4. `setInterval`을 사용하여 `updateTimer` 함수를 1000 밀리초 (1 초) 마다 실행합니다.
5. `setTimeout`을 사용하여 60000 밀리초 (1 분) 후에 타이머를 중지합니다.

이 애플리케이션은 실시간 타이머를 만들기 위해 날짜 차이 함수를 실용적으로 사용하는 것을 보여줍니다.
