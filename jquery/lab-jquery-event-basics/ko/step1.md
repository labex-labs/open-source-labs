# DOM 요소에서 이벤트 응답 설정하기

> `index.html`은 이미 VM 에 제공되어 있습니다.

jQuery 는 페이지 요소에서 이벤트 기반 응답을 설정하는 것을 간단하게 만들어줍니다. 이러한 이벤트는 텍스트가 양식 요소에 입력되거나 마우스 포인터가 이동하는 경우와 같이 최종 사용자의 페이지 상호 작용에 의해 자주 트리거됩니다. 페이지 로드 및 언로드 이벤트와 같은 경우, 브라우저 자체가 이벤트를 트리거합니다.

jQuery 는 대부분의 네이티브 브라우저 이벤트에 대한 편의 메서드를 제공합니다. `.click()`, `.focus()`, `.blur()`, `.change()` 등을 포함하는 이러한 메서드는 jQuery 의 `.on()` 메서드의 축약형입니다. `on` 메서드는 동일한 핸들러 함수를 여러 이벤트에 바인딩하려는 경우, 이벤트 핸들러에 데이터를 제공하려는 경우, 사용자 정의 이벤트를 사용하는 경우 또는 여러 이벤트와 핸들러의 객체를 전달하려는 경우에 유용합니다.

```js
// 편의 메서드를 사용한 이벤트 설정
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// `.on()` 메서드를 사용한 동등한 이벤트 설정
$("p").on("click", function () {
  console.log("click");
});
```

> 웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
