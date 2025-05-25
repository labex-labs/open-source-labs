# 변수 (Variables)

> 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하세요.

변수는 값을 저장하는 컨테이너입니다. `let` 키워드로 변수를 선언하고, 그 뒤에 변수에 부여할 이름을 지정하여 시작합니다.

```js
let myVariable;
```

줄 끝의 세미콜론은 문장이 끝나는 지점을 나타냅니다. 한 줄에 여러 문장을 넣어야 할 때만 필요합니다. 하지만 일부 사람들은 각 문장 끝에 세미콜론을 사용하는 것이 좋은 습관이라고 생각합니다. 세미콜론을 사용해야 하는 경우와 사용하지 않아야 하는 경우에 대한 다른 규칙이 있습니다.

변수 이름은 거의 무엇이든 지정할 수 있지만, 몇 가지 제한 사항이 있습니다. 확실하지 않은 경우, [변수 이름 확인](https://mothereff.in/js-variables)을 통해 유효한지 확인할 수 있습니다.

JavaScript 는 대소문자를 구분합니다. 즉, `myVariable`은 `myvariable`과 동일하지 않습니다. 코드에 문제가 있는 경우, 대소문자를 확인하세요!

변수를 선언한 후, 값을 할당할 수 있습니다.

```js
myVariable = "Bob";
```

또한, 이 두 작업을 같은 줄에서 수행할 수 있습니다.

```js
let myVariable = "Bob";
```

변수 이름을 호출하여 값을 가져올 수 있습니다.

```js
myVariable;
```

변수에 값을 할당한 후, 코드에서 나중에 변경할 수 있습니다.

```js
let myVariable = "Bob";
myVariable = "Steve";
```

변수는 서로 다른 [데이터 타입 (data types)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)의 값을 가질 수 있습니다.

| 변수                                                                 | 설명                                                                                                                | 예시                                                                                                                   |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [String](https://developer.mozilla.org/en-US/docs/Glossary/String)   | 문자열로 알려진 텍스트 시퀀스입니다. 값이 문자열임을 나타내려면 작은따옴표 또는 큰따옴표로 묶습니다.                | `let myVariable = 'Bob';` 또는 `let myVariable = "Bob";`                                                               |
| [Number](https://developer.mozilla.org/en-US/docs/Glossary/Number)   | 숫자입니다. 숫자는 따옴표로 묶지 않습니다.                                                                          | `let myVariable = 10;`                                                                                                 |
| [Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | 참/거짓 값입니다. `true`와 `false`라는 단어는 따옴표가 필요 없는 특별한 키워드입니다.                               | `let myVariable = true;`                                                                                               |
| [Array](https://developer.mozilla.org/en-US/docs/Glossary/Array)     | 단일 참조에 여러 값을 저장할 수 있는 구조입니다.                                                                    | `let myVariable = [1,'Bob','Steve',10];` 배열의 각 멤버를 다음과 같이 참조합니다: `myVariable[0]`, `myVariable[1]` 등. |
| [Object](https://developer.mozilla.org/en-US/docs/Glossary/Object)   | 무엇이든 될 수 있습니다. JavaScript 의 모든 것은 객체이며 변수에 저장할 수 있습니다. 학습하면서 이 점을 기억하세요. | `let myVariable = document.querySelector('h1');` 위의 모든 예시도 마찬가지입니다.                                      |

그렇다면 왜 변수가 필요할까요? 변수는 프로그래밍에서 흥미로운 작업을 수행하는 데 필수적입니다. 값이 변경될 수 없다면, 인사말을 개인화하거나 이미지 갤러리에 표시된 이미지를 변경하는 것과 같은 동적인 작업을 수행할 수 없습니다.
