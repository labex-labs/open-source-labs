# JavaScript 객체 이해하기

객체 키를 소문자로 변환하기 전에, JavaScript 객체가 무엇인지, 그리고 어떻게 작업할 수 있는지 이해해 보겠습니다.

JavaScript 에서 객체는 키 - 값 쌍의 모음입니다. 키는 문자열 (또는 Symbol) 이며, 값은 다른 객체를 포함하여 모든 데이터 유형이 될 수 있습니다.

Node.js 대화형 셸을 열어 시작해 보겠습니다.

1. WebIDE 에서 터미널을 엽니다.
2. `node`를 입력하고 Enter 키를 누릅니다.

이제 JavaScript 코드를 직접 입력할 수 있는 Node.js 프롬프트 (`>`) 가 표시됩니다.

대소문자가 혼합된 키를 가진 간단한 객체를 만들어 보겠습니다.

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

이 코드를 Node.js 프롬프트에 입력하고 Enter 키를 누릅니다. 객체를 보려면 `user`를 입력하고 Enter 키를 누릅니다.

```javascript
user;
```

다음과 같은 출력을 볼 수 있습니다.

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

보시다시피, 이 객체는 서로 다른 대소문자 스타일의 키를 가지고 있습니다. 다음 단계에서는 이러한 키에 액세스하고 소문자로 변환하는 방법을 배웁니다.
