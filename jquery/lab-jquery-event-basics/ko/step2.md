# 새로운 페이지 요소로 이벤트 확장하기

`.on()`은 리스너를 설정하는 시점에 존재하는 요소에 대해서만 이벤트 리스너를 생성할 수 있다는 점을 기억하는 것이 중요합니다. 예를 들어:

```js
$(document).ready(function () {
  // Now create a new button element with the alert class.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Sets up click behavior on all button elements with the alert class
  // that exist in the DOM when the instruction was executed
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

이벤트 리스너가 설정된 후에 유사한 요소가 생성되면, 이전에 설정한 이벤트 동작을 자동으로 가져오지 않습니다.

> **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
