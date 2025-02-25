# Установить перспективные проекции

Установите второй подграфик для использования перспективной проекции с стандартным углом обзора (`FOV`) 90 градусов и длиной фокуса (`focal_length`) 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Установите третий подграфик для использования перспективной проекции с углом обзора (`FOV`) 157.4 градуса и длиной фокуса (`focal_length`) 0.2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
