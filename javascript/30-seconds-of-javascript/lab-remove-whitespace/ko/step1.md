# 공백 제거 함수

문자열에서 공백을 제거하려면 다음 함수를 사용하십시오.

- 정규 표현식 (regular expression) 과 함께 `String.prototype.replace()`를 사용하여 모든 공백 문자를 빈 문자열로 바꿉니다.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## 정규 표현식 설명

- `/\s+/g`는 다음과 같이 분석됩니다.
  - `\s`: 모든 공백 문자 (공백, 탭, 줄 바꿈) 와 일치합니다.
  - `+`: 이전 문자가 하나 이상 나타나는 경우와 일치합니다.
  - `/g`: 전역 플래그 (global flag) - 문자열의 첫 번째 발생뿐만 아니라 모든 발생과 일치합니다.

## 빠른 정규 표현식 참조

일반적인 공백 패턴:

- `\s` - 모든 공백 (공백, 탭, 줄 바꿈) 과 일치합니다.
- `\t` - 탭 문자와 일치합니다.
- `\n` - 줄 바꿈 문자와 일치합니다.
- `\r` - 캐리지 리턴 (carriage return) 과 일치합니다.
- `` (공백) - 공백 문자만 일치합니다.

예를 들어,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// 추가 예시:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
