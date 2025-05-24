# Box-Sizing Reset

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

요소의 `width`와 `height`가 `border` 또는 `padding`의 영향을 받지 않도록 하려면 `box-sizing: border-box` CSS 속성을 사용하십시오. 이는 요소의 `width`와 `height` 계산에 `padding`과 `border`를 포함합니다. 부모 요소에서 `box-sizing` 속성을 상속받으려면 `box-sizing: inherit`를 사용하십시오.

다음은 두 개의 `div` 요소를 사용하여 `box-sizing` 속성을 사용하는 예입니다.

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

이 예에서 첫 번째 `div` 요소는 `box-sizing: border-box`를 가지고, 두 번째 `div` 요소는 `box-sizing: content-box`를 가지고 있습니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
