### Error Message on apple silicon Python 3.9.6

```
Traceback (most recent call last):
  File "/Users/zheng/Works/tmp/multiprocessing-initializer/poc.py", line 14, in <module>
    future_to_calculate = {executor.submit(concurrent_func, i) : i for i in nums}
  File "/Users/zheng/Works/tmp/multiprocessing-initializer/poc.py", line 14, in <dictcomp>
    future_to_calculate = {executor.submit(concurrent_func, i) : i for i in nums}
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/concurrent/futures/process.py", line 697, in submit
    self._adjust_process_count()
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/concurrent/futures/process.py", line 675, in _adjust_process_count
    p.start()
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/process.py", line 121, in start
    self._popen = self._Popen(self)
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/context.py", line 284, in _Popen
    return Popen(process_obj)
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/popen_spawn_posix.py", line 32, in __init__
    super().__init__(process_obj)
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/popen_fork.py", line 19, in __init__
    self._launch(process_obj)
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/popen_spawn_posix.py", line 47, in _launch
    reduction.dump(process_obj, fp)
  File "/Users/zheng/.pyenv/versions/3.9.6/lib/python3.9/multiprocessing/reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
AttributeError: Can't pickle local object 'create_engine.<locals>.connect'
```