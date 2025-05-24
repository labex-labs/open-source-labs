# 카운터 (Counter)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

중첩된 목록 요소를 고려하는 사용자 정의 목록 카운터를 만들려면 다음 단계를 따르세요.

1. `counter-reset`을 사용하여 변수 카운터 (기본값 `0`) 를 초기화합니다. 이름은 속성의 값 (예: `counter`) 입니다.
2. 각 계산 가능한 요소 (예: 각 `<li>`) 에 대해 변수 카운터에 `counter-increment`를 사용합니다.
3. 각 계산 가능한 요소 (예: 각 `<li>`) 에 대한 `::before` 가상 요소의 `content`의 일부로 각 변수 카운터의 값을 표시하려면 `counters()`를 사용합니다. 여기에 전달된 두 번째 값 (`'.'`) 은 중첩된 카운터의 구분 기호 역할을 합니다.

다음은 HTML 코드의 예입니다.

```html
<ul>
  <li>List item</li>
  <li>List item</li>
  <li>
    List item
    <ul>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
  </li>
</ul>
```

다음은 사용자 정의 목록 카운터를 적용하는 CSS 코드입니다.

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
