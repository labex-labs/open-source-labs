# Pascal Case 이해 및 환경 설정

Pascal case 는 다음과 같은 명명 규칙입니다.

- 각 단어의 첫 글자는 대문자로 표기합니다.
- 단어 사이에 공백, 하이픈 또는 밑줄을 사용하지 않습니다.
- 나머지 글자는 소문자로 표기합니다.

예를 들어:

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

개발 환경을 설정하는 것으로 시작해 보겠습니다.

1. WebIDE 인터페이스에서 상단 메뉴 바의 "Terminal"을 클릭하여 터미널을 엽니다.

2. 터미널에 다음 명령을 입력하고 Enter 키를 눌러 Node.js 대화형 세션을 시작합니다.

```bash
node
```

Node.js 프롬프트 (`>`) 가 나타나면 Node.js 대화형 환경에 진입한 것입니다.

3. 간단한 문자열 조작을 시도하여 몸을 풀어보겠습니다. Node.js 프롬프트에 다음 코드를 입력합니다.

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

출력 결과는 다음과 같습니다.

```
John doe
```

이 간단한 예제는 문자열의 첫 글자를 대문자로 변환하는 방법을 보여줍니다. 다음을 사용했습니다.

- `charAt(0)`: 첫 번째 문자를 가져옵니다.
- `toUpperCase()`: 대문자로 변환합니다.
- `slice(1)`: 나머지 문자열을 가져옵니다.
- `+`를 사용한 연결 (concatenation): 문자열을 결합합니다.

이러한 문자열 메서드는 Pascal case 변환기를 만들 때 유용할 것입니다.
