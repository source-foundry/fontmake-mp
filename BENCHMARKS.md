The benchmarks displayed on the README.md page were executed with the following:

### System

- MacBook Pro (Retina, 15-inch, Mid 2015)
- 2.8 GHz Intel Core i7
- 16 GB 1600 MHz DDR3
- macOS 10.12.6


### Python

- cPython 3.6.3
- PyPy 5.9.0


### fontmake

- fontmake v1.3.0


### UFO source files

- all four variants of the Hack UFO source in the [tests directory](tests) of this repository


### Timing methodology

For single core sequential compile testing:

```
$ /usr/bin/time -p python3 benchmark.py
```

For cPython parallel compile testing:

```
$ /usr/bin/time -p python3 fmp.py tests/*.ufo
```


For PyPy parallel compile testing:

(from PyPy virtualenv)

```
$ /usr/bin/time -p python fmp.py tests/*.ufo
```

The results (in seconds) represent elapsed time over these test trial runs.

### Test trials

Testing was performed in three trials for each test condition and the data in the figure represents the mean of these three values (in sec).

