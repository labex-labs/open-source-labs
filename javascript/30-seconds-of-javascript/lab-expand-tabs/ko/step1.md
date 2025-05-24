# JavaScript 에서 탭을 공백으로 변환하는 방법

코딩 시 탭 문자를 공백으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.replace()` 메서드를 정규 표현식 (regular expression) 과 `String.prototype.repeat()`와 함께 사용하여 각 탭 문자를 원하는 수의 공백으로 대체합니다.
3. 아래 코드 조각은 `expandTabs` 함수를 사용하여 탭을 공백으로 바꾸는 방법을 보여줍니다.

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

위의 예에서 `expandTabs` 함수는 두 개의 인수를 받습니다. 탭을 포함하는 문자열 `str`과 각 탭 문자를 대체할 공백의 수를 나타내는 숫자 `count`입니다. 이 함수는 `String.prototype.replace()` 메서드를 정규 표현식 (`/\t/g`) 과 함께 사용하여 입력 문자열에서 모든 탭 문자를 찾아 `String.prototype.repeat()` 메서드를 사용하여 원하는 수의 공백으로 대체합니다.
