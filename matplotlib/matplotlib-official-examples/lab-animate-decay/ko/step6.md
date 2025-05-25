# 애니메이션 생성

마지막으로, `FuncAnimation` 클래스를 사용하여 애니메이션을 생성할 수 있습니다. 애니메이션을 생성하기 위해 `fig`, `run`, `data_gen`, `init_func`, 및 `interval` 매개변수를 전달합니다. 또한 마지막 100 개의 프레임만 저장되도록 `save_count` 매개변수를 100 으로 설정합니다.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
