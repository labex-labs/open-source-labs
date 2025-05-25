# 여러 이벤트 응답 설정하기

응용 프로그램의 요소는 여러 이벤트에 바인딩되는 경우가 많습니다. 여러 이벤트가 동일한 핸들링 함수를 공유해야 하는 경우, `.on()`에 공백으로 구분된 이벤트 유형 목록을 제공할 수 있습니다.

```js
// Multiple events, same handler
$("div").on(
  "click change", // Bind handlers for multiple events
  function () {
    console.log("An input was clicked or changed!");
  }
);
```

각 이벤트가 자체 핸들러를 갖는 경우, 이벤트 이름이 키이고 이벤트 처리를 위한 함수가 값인 하나 이상의 키/값 쌍을 사용하여 객체를 `.on()`에 전달할 수 있습니다.

```js
// Binding multiple events with different handlers
$("div").on({
  click: function () {
    console.log("clicked!");
  },
  mouseover: function () {
    console.log("hovered!");
  }
});
```

> **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
