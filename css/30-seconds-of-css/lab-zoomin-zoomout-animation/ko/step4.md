# 애니메이션 적용

이제 keyframes (키프레임) 을 정의했으므로, 애니메이션을 상자 요소에 적용해야 합니다.

1. `style.css` 파일을 다시 열고 `.zoom-in-out-box` 선택자를 다음과 같이 수정합니다:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. 추가한 animation (애니메이션) 속성을 이해해 봅시다:
   - `animation`은 여러 animation (애니메이션) 속성을 한 번에 설정하는 shorthand property (단축 속성) 입니다.
   - `zoom-in-zoom-out`은 keyframes (키프레임) 애니메이션의 이름입니다.
   - `1s`는 애니메이션의 한 주기가 1 초 동안 지속되도록 지정합니다.
   - `ease`는 애니메이션이 천천히 시작하여 속도가 빨라진 다음 다시 느려지도록 하는 timing function (타이밍 함수) 입니다.
   - `infinite`는 애니메이션이 영원히 반복됨을 의미합니다.

3. 이러한 변경 사항을 적용한 후 `style.css` 파일을 저장합니다.

4. 웹 서버가 이미 실행 중인 경우, **Web 8080** 탭을 새로 고치기만 하면 됩니다. 그렇지 않은 경우, 오른쪽 하단 모서리에 있는 "Go Live"를 클릭하여 서버를 시작한 다음 **Web 8080** 탭을 엽니다.

이제 분홍색 사각형이 부드럽게 줌 인 및 줌 아웃되는 연속적인 애니메이션을 볼 수 있습니다. 사각형은 원래 크기의 1.5 배에 도달할 때까지 커진 다음 정상 크기로 다시 축소됩니다. 이 주기는 무한히 반복됩니다.
