# Definir as Funções

Definiremos três funções que usaremos para criar o diagrama.

#### Função Problems

A primeira função é a função problems. Esta função recebe o nome da categoria, as posições x e y da seta do problema e o ângulo da anotação do problema. Ela usa o método annotate para criar a seta e a anotação do problema.

```python
def problems(data: str,
             problem_x: float, problem_y: float,
             prob_angle_x: float, prob_angle_y: float):
    ax.annotate(str.upper(data), xy=(problem_x, problem_y),
                xytext=(prob_angle_x, prob_angle_y),
                fontsize='10',
                color='white',
                weight='bold',
                xycoords='data',
                verticalalignment='center',
                horizontalalignment='center',
                textcoords='offset fontsize',
                arrowprops=dict(arrowstyle="->", facecolor='black'),
                bbox=dict(boxstyle='square',
                          facecolor='tab:blue',
                          pad=0.8))
```

#### Função Causes

A segunda função é a função causes. Esta função recebe a lista de causas, as posições x e y da anotação da causa e se a causa deve ser colocada acima ou abaixo da seta do problema. Ela usa o método annotate para criar a anotação e a seta da causa.

```python
def causes(data: list, cause_x: float, cause_y: float,
           cause_xytext=(-9, -0.3), top: bool = True):
    for index, cause in enumerate(data):
        coords = [[0, [0, 0]],
                  [0.23, [0.5, -0.5]],
                  [-0.46, [-1, 1]],
                  [0.69, [1.5, -1.5]],
                  [-0.92, [-2, 2]],
                  [1.15, [2.5, -2.5]]]
        if top:
            cause_y += coords[index][1][0]
        else:
            cause_y += coords[index][1][1]
        cause_x -= coords[index][0]
        ax.annotate(cause, xy=(cause_x, cause_y),
                    horizontalalignment='center',
                    xytext=cause_xytext,
                    fontsize='9',
                    xycoords='data',
                    textcoords='offset fontsize',
                    arrowprops=dict(arrowstyle="->",
                                    facecolor='black'))
```

#### Função Draw Body

A terceira função é a função draw body. Esta função recebe os dados de entrada e os usa para criar o diagrama de Ishikawa (fishbone diagram).

```python
def draw_body(data: dict):
    second_sections = []
    third_sections = []
    if len(data) == 1 or len(data) == 2:
        spine_length = (-2.1, 2)
        head_pos = (2, 0)
        tail_pos = ((-2.8, 0.8), (-2.8, -0.8), (-2.0, -0.01))
        first_section = [1.6, 0.8]
    elif len(data) == 3 or len(data) == 4:
        spine_length = (-3.1, 3)
        head_pos = (3, 0)
        tail_pos = ((-3.8, 0.8), (-3.8, -0.8), (-3.0, -0.01))
        first_section = [2.6, 1.8]
        second_sections = [-0.4, -1.2]
    else:  # len(data) == 5 or 6
        spine_length = (-4.1, 4)
        head_pos = (4, 0)
        tail_pos = ((-4.8, 0.8), (-4.8, -0.8), (-4.0, -0.01))
        first_section = [3.5, 2.7]
        second_sections = [1, 0.2]
        third_sections = [-1.5, -2.3]

    for index, problem in enumerate(data.values()):
        top_row = True
        cause_arrow_y = 1.7
        if index % 2 != 0:
            top_row = False
            y_prob_angle = -16
            cause_arrow_y = -1.7
        else:
            y_prob_angle = 16
        if index in (0, 1):
            prob_arrow_x = first_section[0]
            cause_arrow_x = first_section[1]
        elif index in (2, 3):
            prob_arrow_x = second_sections[0]
            cause_arrow_x = second_sections[1]
        else:
            prob_arrow_x = third_sections[0]
            cause_arrow_x = third_sections[1]
        if index > 5:
            raise ValueError(f'Maximum number of problems is 6, you have entered '
                             f'{len(data)}')
        ax.plot(spine_length, [0, 0], color='tab:blue', linewidth=2)
        ax.text(head_pos[0] + 0.1, head_pos[1] - 0.05, 'PROBLEM', fontsize=10,
                weight='bold', color='white')
        semicircle = Wedge(head_pos, 1, 270, 90, fc='tab:blue')
        ax.add_patch(semicircle)
        triangle = Polygon(tail_pos, fc='tab:blue')
        ax.add_patch(triangle)
        problems(list(data.keys())[index], prob_arrow_x, 0, -12, y_prob_angle)
        causes(problem, cause_arrow_x, cause_arrow_y, top=top_row)
```
