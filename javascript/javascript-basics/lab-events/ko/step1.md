# 이벤트 (Events)

> `index.html`은 이미 VM 에 제공되어 있습니다.

웹사이트에서 실제 상호 작용을 위해서는 이벤트 핸들러가 필요합니다. 이벤트 핸들러는 브라우저에서 활동을 감지하고 그에 따라 코드를 실행하는 코드 구조입니다. 가장 명확한 예는 마우스로 무언가를 클릭할 때 브라우저에서 발생하는 [click event](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event)를 처리하는 것입니다. 이를 시연하기 위해 다음 코드를 콘솔에 입력한 다음 현재 웹 페이지를 클릭하십시오.

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

요소에 이벤트 핸들러를 연결하는 방법에는 여러 가지가 있습니다.
여기서는 [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html) 요소를 선택합니다. 그런 다음, 수신할 이벤트의 이름 (`'click'`) 과 이벤트가 발생할 때 실행할 함수를 전달하여 [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) 함수를 호출합니다.

방금 `addEventListener()`에 전달한 함수는 이름이 없기 때문에 *익명 함수*라고 합니다. 익명 함수를 작성하는 다른 방법이 있으며, 이를 *화살표 함수*라고 합니다.
화살표 함수는 `function ()` 대신 `() =>`를 사용합니다.

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

> 웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
