# 애니메이션 생성

`matplotlib.animation`의 `FuncAnimation` 클래스를 사용하여 애니메이션을 생성합니다. `FuncAnimation` 생성자에 figure 객체, 업데이트 함수, 총 프레임 수 (랜덤 워크의 단계 수와 같음), 모든 랜덤 워크의 리스트, 그리고 모든 선의 리스트를 인수로 전달합니다.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
