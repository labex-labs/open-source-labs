# 물방울 무늬 배경 패턴

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

물방울 무늬 배경 패턴을 만들려면 다음 단계를 따르세요.

1. `background-color` 속성을 검정색으로 설정합니다.
2. 두 개의 점을 만들기 위해 `radial-gradient()` 값을 두 개 사용하여 `background-image` 속성을 사용합니다.
3. `background-size` 속성을 사용하여 패턴의 크기를 지정합니다. `background-position`을 사용하여 두 그라데이션을 적절하게 배치합니다.
4. `background-repeat`를 `repeat`로 설정합니다.
5. 요소의 고정된 `height`와 `width`는 데모 목적으로만 사용됩니다.

다음은 클래스 `polka-dot`을 가진 div 요소에 대한 HTML 코드 예시입니다.

```html
<div class="polka-dot"></div>
```

다음은 해당 CSS 코드입니다.

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
