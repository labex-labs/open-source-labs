# Define UpdateDist Class

Next, we define a class called `UpdateDist` that will be used to update the beta distribution as new data is observed. The `UpdateDist` class takes two arguments: the Matplotlib axis object and the initial probability of success.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')
```

The `__init__` method initializes the class instance by setting the initial number of successes to zero (`self.success = 0`) and the initial probability of success to the value passed as an argument (`self.prob = prob`). We also create a line object to represent the beta distribution and set up the plot parameters.

The `__call__` method is called every time the animation updates. It simulates a coin toss experiment and updates the beta distribution accordingly.

```python
def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

If this is the first frame of the animation (`if i == 0`), we reset the number of successes to zero and clear the line object. Otherwise, we simulate a coin toss experiment by generating a random number between 0 and 1 (`np.random.rand()`) and comparing it to the probability of success (`self.prob`). If the random number is less than the probability of success, we count it as a success and update the beta distribution using the `beta_pdf` function. Finally, we update the line object with the new data and return it.
