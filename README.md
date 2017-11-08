# fontmake-mp [![Build Status](https://semaphoreci.com/api/v1/sourcefoundry/fontmake-mp/branches/master/badge.svg)](https://semaphoreci.com/sourcefoundry/fontmake-mp)


## About

fontmake-mp is a Python script (`fmp.py`) that adds parallel UFO source compilation support to the [fontmake](https://github.com/googlei18n/fontmake) font compiler.  It supports automation of parallel UFO compilation up to the number of available cores on your system.

And it makes a difference.



<img src="https://github.com/source-foundry/fontmake-mp/raw/master/img/benchmarks-crunch.png" alt="fontmake-mp benchmarks" />



## Install

### Install fontmake
fontmake must be installed on your system to use this script.  You can install fontmake with the command:

```
$ pip install fontmake
```

### Download the fmp.py script

Download the executable Python script with either of the following approaches:

##### 1. cURL approach

Use cURL to pull `fmp.py` to the location where you would like to execute the file:
 
```
$ curl -L -O https://raw.githubusercontent.com/source-foundry/fontmake-mp/master/fmp.py
```

##### 2. Download and unpack .zip archive

[Download the .zip archive of the source repository](https://github.com/source-foundry/fontmake-mp/archive/master.zip), unpack it, and move the `fmp.py` script to the location of your choice on your system. You can discard all other repository files and the unpacked repository directory.

## Usage

By default, `fmp.py` build both `.ttf` and `.otf` fonts during the compilation process.  This can be modified as necessary to one or the other of these file types (see Manual modifications section below). 

The format for command line usage is the following:

```
$ python fmp.py [UFO path 1] [UFO path 2] ... [UFO path n]
```

Faster compiles can be achieved for some users with the use of the PyPy interpreter rather than the cPython interpreter.  Install [PyPy](http://pypy.org/) on your system and execute the script with the following command:

```
$ pypy fmp.py [UFO path 1] [UFO path 2] ... [UFO path n]
```

`fmp.py` will spawn a new process for each UFO source directory of multi-font builds up to the number of available cores on your system as determined by the Python `multiprocessing.cpu_count()` method.

### Manual modifications

#### Change spawned process number

To manually set the spawned process number, modify the `PROCESSES` constant integer at the top of the `fmp.py` file to the desired number of processes.


#### Change build file type

The build file type can be modified in the `BUILD_FILE_TYPE` constant at the top of the `fmp.py` file.  This should be formatted as a Python tuple.  Use the following settings to modify your build:

##### ttf files only

```python
BUILD_FILE_TYPE = ('ttf')
```

##### otf files only

```python
BUILD_FILE_TYPE = ('otf')
```

## Acknowledgments

fontmake-mp is a script built on the excellent [fontmake](https://github.com/googlei18n/fontmake) project where all of the hard work happens.

## License

[MIT license](https://github.com/source-foundry/fontmake-mp/blob/master/LICENSE.md)