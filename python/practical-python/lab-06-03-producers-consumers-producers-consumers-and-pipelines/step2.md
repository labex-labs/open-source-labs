# Generator Pipelines

You can use this aspect of generators to set up processing pipelines (like Unix pipes).

_producer_ → _processing_ → _processing_ → _consumer_

Processing pipes have an initial data producer, some set of intermediate processing stages and a final consumer.

**producer** → _processing_ → _processing_ → _consumer_

```python
def producer():
    ...
    yield item
    ...
```

The producer is typically a generator. Although it could also be a list of some other sequence. `yield` feeds data into the pipeline.

_producer_ → _processing_ → _processing_ → **consumer**

```python
def consumer(s):
    for item in s:
        ...
```

Consumer is a for-loop. It gets items and does something with them.

_producer_ → **processing** → **processing** → _consumer_

```python
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
```

Intermediate processing stages simultaneously consume and produce items. They might modify the data stream. They can also filter (discarding items).

_producer_ → _processing_ → _processing_ → _consumer_

```python
def producer():
    ...
    yield item          # yields the item that is received by the `processing`
    ...

def processing(s):
    for item in s:      # Comes from the `producer`
        ...
        yield newitem   # yields a new item
        ...

def consumer(s):
    for item in s:      # Comes from the `processing`
        ...
```

Code to setup the pipeline

```python
a = producer()
b = processing(a)
c = consumer(b)
```

You will notice that data incrementally flows through the different functions.

For this exercise the `stocksim.py` program should still be running in the background. You're going to use the `follow()` function you wrote in the previous exercise.
