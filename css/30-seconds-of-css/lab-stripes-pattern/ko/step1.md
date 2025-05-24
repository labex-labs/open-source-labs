# 스트라이프 배경 패턴

`index.html`과 `style.css`는 이미 VM 에 제공되었습니다.

이 코드는 흰색 배경에 수직 스트라이프 패턴을 생성합니다.

패턴을 생성하려면:

- `background-color` 속성을 흰색으로 설정합니다.
- `linear-gradient()` 값을 사용하여 `background-image`를 사용하여 수직 스트라이프를 생성합니다.
- `background-size` 속성을 설정하여 각 스트라이프의 크기를 지정합니다.
- `background-repeat`를 `repeat`로 설정하여 패턴이 요소를 채우도록 합니다.

요소의 고정된 `width`와 `height`는 데모 목적으로만 사용됩니다.

다음은 코드 스니펫 예시입니다:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
