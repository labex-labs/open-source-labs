# 플롯 설정

새로운 figure 와 axis 객체를 생성하고 Scope 클래스를 초기화합니다. 그런 다음 update 및 emitter 함수를 FuncAnimation 메서드에 전달하여 애니메이션을 생성합니다.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
