# Clearfix

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

`float`를 사용하여 레이아웃을 구축할 때 요소가 자체적으로 자식 요소를 정리하도록 하려면, `::after` 가상 요소 (pseudo-element) 를 사용하고 `content: ''`를 적용하여 레이아웃에 영향을 미치도록 할 수 있습니다. 또한, `clear: both`를 사용하여 요소가 왼쪽 및 오른쪽 플로트 모두를 지나 정리하도록 합니다. 그러나 이 기법은 컨테이너에 플로팅되지 않은 자식 요소가 없고, clearfixed 컨테이너 앞에 키가 큰 플로트가 없지만 동일한 서식 컨텍스트 (예: 플로팅된 열) 에 있는 경우에만 제대로 작동합니다. 예를 들어:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

플로트를 사용하여 레이아웃을 구축하는 것보다 flexbox 또는 grid 레이아웃과 같은 더 현대적인 접근 방식을 사용하는 것이 좋습니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
