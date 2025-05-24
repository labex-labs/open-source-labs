# 호버 그림자 상자 애니메이션

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

텍스트에 마우스를 올렸을 때 그림자 상자를 만들려면 다음 단계를 따르세요.

1. `transform: perspective(1px)`를 설정하여 요소에 3D 공간을 부여하고, Z 평면과 사용자 간의 거리에 영향을 미치며, `translateZ(0)`을 사용하여 3D 공간에서 z 축을 따라 `p` 요소를 재배치합니다.
2. `box-shadow`를 사용하여 상자를 투명하게 만듭니다.
3. `transition-property` 속성을 사용하여 `box-shadow`와 `transform` 모두에 대해 전환 (transition) 을 활성화합니다.
4. `:hover`, `:active`, `:focus` 의사 클래스 선택자 (pseudo-class selector) 를 사용하여 새로운 `box-shadow`와 `transform: scale(1.2)`를 적용하여 텍스트의 크기를 변경합니다.
5. `p` 요소에 `hover-shadow-box-animation` 클래스를 추가합니다.

다음은 HTML 코드입니다.

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

다음은 CSS 코드입니다.

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
