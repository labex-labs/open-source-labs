# ISO 형식 날짜 문자열을 검증하는 함수 생성

이 단계에서는 주어진 문자열이 유효한 ISO 8601 형식인지 확인하는 JavaScript 함수를 생성합니다.

## 검증 함수 생성

ISO 날짜 검증기를 위한 새로운 JavaScript 파일을 생성해 보겠습니다.

1. WebIDE 에서 왼쪽 사이드바의 탐색기 아이콘을 클릭합니다.
2. 파일 탐색기에서 마우스 오른쪽 버튼을 클릭하고 "새 파일"을 선택합니다.
3. 파일 이름을 `isISODate.js`로 지정하고 Enter 키를 누릅니다.
4. 파일에 다음 코드를 추가합니다.

```javascript
/**
 * 문자열이 유효한 ISO 8601 형식의 날짜 문자열인지 확인합니다.
 * @param {string} val - 확인할 문자열
 * @return {boolean} - 문자열이 ISO 형식인 경우 true 를 반환하고, 그렇지 않으면 false 를 반환합니다.
 */
const isISOString = (val) => {
  // 입력 문자열에서 Date 객체를 생성합니다.
  const d = new Date(val);

  // 날짜가 유효한지 (NaN 이 아닌지) 와 ISO 문자열이 원본과 일치하는지 확인합니다.
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// 다른 곳에서 사용할 수 있도록 함수를 내보냅니다.
module.exports = isISOString;
```

이 함수가 어떻게 작동하는지 살펴보겠습니다.

1. `new Date(val)`은 입력 문자열에서 Date 객체를 생성합니다.
2. `d.valueOf()`는 숫자 타임스탬프 값 (1970 년 1 월 1 일 이후의 밀리초) 을 반환합니다.
3. `Number.isNaN(d.valueOf())`는 날짜가 유효하지 않은지 (NaN 은 "Not a Number"를 의미) 확인합니다.
4. `d.toISOString() === val`은 Date 를 다시 ISO 문자열로 변환한 것이 원래 입력과 일치하는지 확인합니다.

## 함수 테스트

이제 함수를 테스트하기 위해 간단한 테스트 파일을 생성해 보겠습니다.

1. `testISO.js`라는 다른 파일을 생성합니다.
2. 다음 코드를 추가합니다.

```javascript
// isISOString 함수를 가져옵니다.
const isISOString = require("./isISODate");

// 유효한 ISO 형식 날짜로 테스트합니다.
console.log("유효한 ISO 날짜 테스트:");
console.log("2020-10-12T10:10:10.000Z");
console.log("결과:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// 유효하지 않은 형식으로 테스트합니다.
console.log("ISO 가 아닌 날짜 테스트:");
console.log("2020-10-12");
console.log("결과:", isISOString("2020-10-12"));
```

3. Node.js 를 사용하여 테스트 파일을 실행합니다.

```bash
node testISO.js
```

다음과 유사한 출력을 볼 수 있습니다.

```
유효한 ISO 날짜 테스트:
2020-10-12T10:10:10.000Z
결과: true

ISO가 아닌 날짜 테스트:
2020-10-12
결과: false
```

이것은 우리 함수가 "2020-10-12T10:10:10.000Z"가 유효한 ISO 형식 날짜이고 "2020-10-12"는 그렇지 않다는 것을 올바르게 식별하는 것을 보여줍니다.
