# 함수 (Functions)

> `index.html`은 이미 VM 에 제공되어 있습니다.

[함수 (Functions)](https://developer.mozilla.org/en-US/docs/Glossary/Function)는 재사용하려는 기능을 패키징하는 방법입니다. 코드의 함수 이름을 호출할 때 실행되는 코드 본문을 함수로 정의할 수 있습니다. 이는 동일한 코드를 반복적으로 작성하는 대신 사용할 수 있는 좋은 방법입니다. 이미 함수의 몇 가지 사용법을 보셨습니다.

예를 들어:

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

이러한 함수, `document.querySelector` 및 `alert`는 브라우저에 내장되어 있습니다.

> 웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

변수 이름처럼 보이지만 괄호— `()` —가 뒤따르는 경우, 이는 함수일 가능성이 높습니다. 함수는 종종 [인수 (arguments)](https://developer.mozilla.org/en-US/docs/Glossary/Argument)를 받습니다. 즉, 작업을 수행하는 데 필요한 데이터 조각입니다. 인수는 괄호 안에 들어가며, 인수가 두 개 이상인 경우 쉼표로 구분됩니다.

예를 들어, `alert()` 함수는 브라우저 창 안에 팝업 상자를 표시하지만, 표시할 메시지를 함수에 알려주기 위해 문자열을 인수로 제공해야 합니다.

자신만의 함수를 정의할 수도 있습니다.

다음 예제에서는 두 개의 숫자를 인수로 받아 곱하는 간단한 함수를 만듭니다.

> 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하십시오.

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

콘솔에서 이 코드를 실행해보고 여러 인수로 테스트해 보십시오. 예를 들어:

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **참고:** [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return) 문은 브라우저에게 `result` 변수를 함수 밖으로 반환하여 사용할 수 있도록 합니다. 이는 함수 내에서 정의된 변수는 해당 함수 내에서만 사용할 수 있기 때문에 필요합니다. 이를 변수 스코핑 (variable scoping) 이라고 합니다. ( [변수 스코핑 (variable scoping)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope)에 대해 자세히 알아보십시오.)
