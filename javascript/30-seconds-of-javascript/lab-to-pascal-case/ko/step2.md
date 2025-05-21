# 단어 분리를 위한 정규 표현식 (Regular Expressions) 사용

문자열을 Pascal case 로 변환하려면 첫 번째 단계는 문자열을 개별 단어로 분리하는 것입니다. 사용된 구분 기호 (공백, 하이픈, 밑줄 등) 에 관계없이 단어 경계를 식별하기 위해 정규 표현식 (regex) 을 사용할 수 있습니다.

JavaScript 에서 정규 표현식은 슬래시 (`/pattern/`) 로 묶입니다. 정규 표현식을 사용하여 문자열을 단어로 분리하는 방법을 살펴보겠습니다.

1. Node.js 세션에서 먼저 간단한 예제를 시도해 보겠습니다. 다음 코드를 입력합니다.

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

출력 결과는 다음과 같습니다.

```
[ 'hello', 'world', 'example' ]
```

이 정규 표현식 `/[-_]/`는 하이픈 또는 밑줄과 일치하며, `split()`은 이러한 일치를 구분 기호로 사용합니다.

2. 이제 더 복잡한 문자열과 정규 표현식을 시도해 보겠습니다. 다음을 입력합니다.

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

출력 결과는 다음과 같습니다.

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

이 정규 표현식을 분석해 보겠습니다.

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`: 대문자 시퀀스를 일치시킵니다.
- `/[A-Z]?[a-z]+[0-9]*/`: 대문자로 시작할 수 있는 단어를 일치시킵니다.
- `/[A-Z]/`: 단일 대문자를 일치시킵니다.
- `/[0-9]+/`: 숫자 시퀀스를 일치시킵니다.
- `g` 플래그는 일치를 전역적으로 만듭니다 (모든 일치 항목을 찾습니다).

`match()` 메서드는 문자열에서 찾은 모든 일치 항목의 배열을 반환합니다. 이 메서드는 거의 모든 형식의 단어를 식별할 수 있으므로 Pascal case 변환기에 필수적입니다.
