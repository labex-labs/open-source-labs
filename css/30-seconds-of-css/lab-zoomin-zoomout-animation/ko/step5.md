# 애니메이션 속성 실험

다양한 animation (애니메이션) 속성을 실험하여 애니메이션을 사용자 정의해 보겠습니다. 이를 통해 이러한 속성이 애니메이션 동작에 어떤 영향을 미치는지 이해할 수 있습니다.

1. `style.css` 파일을 열고 `.zoom-in-out-box` 선택자를 수정하여 다양한 animation (애니메이션) 속성을 시도해 봅니다:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. 변경한 내용을 이해해 봅시다:
   - animation duration (애니메이션 지속 시간) 을 `2s` (2 초) 로 연장했습니다.
   - timing function (타이밍 함수) 을 `ease-in-out`으로 변경하여 애니메이션의 시작과 끝을 모두 부드럽게 만들었습니다.
   - 상자의 모서리를 둥글게 만들기 위해 `border-radius`를 10px 로 추가했습니다.

3. 회전 효과를 추가하기 위해 keyframes (키프레임) 도 수정해 보겠습니다:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. 이 업데이트된 keyframes (키프레임) 정의에서:
   - `transform` 속성에 `rotate()` 함수를 추가했습니다.
   - 50% 지점에서 요소는 확대되면서 45 도 회전합니다.
   - 또한 50% 지점에서 배경색을 파란색으로 변경합니다.

5. 이러한 변경 사항을 적용한 후 `style.css` 파일을 저장합니다.

6. 향상된 애니메이션을 보려면 **Web 8080** 탭을 새로 고칩니다.

이제 애니메이션은 더 느리고 (주기당 2 초), 둥근 모서리를 가지며, 줌하는 동안 회전하고, 애니메이션 중간에 색상이 변경되어야 합니다. 이는 CSS 애니메이션이 풍부한 시각적 효과를 위해 여러 속성 변경을 결합할 수 있음을 보여줍니다.

다양한 속성과 값을 더 실험하여 애니메이션에 어떤 영향을 미치는지 자유롭게 확인해 보세요.
