# Hive_kernel
Hive  Kernel for Jupyter

![PyPI version](https://img.shields.io/pypi/pyversions/hive_kernel.svg)
![Github license](https://img.shields.io/github/license/Hourout/hive_kernel.svg)
[![PyPI](https://img.shields.io/pypi/v/hive_kernel.svg)](https://pypi.python.org/pypi/hive_kernel)
![PyPI format](https://img.shields.io/pypi/format/hive_kernel.svg)
![contributors](https://img.shields.io/github/contributors/Hourout/hive_kernel)
![downloads](https://img.shields.io/pypi/dm/hive_kernel.svg)


[中文介绍](document/chinese.md)

## Installation

#### step1:
```
pip install hive_kernel
```

To get the newest one from this repo (note that we are in the alpha stage, so there may be frequent updates), type:

```
pip install git+git://github.com/Hourout/hive_kernel.git
```

#### step2:
Add kernel to your jupyter:

```
python -m hive_kernel.install
```

ALL DONE! 🎉🎉🎉

## Uninstall

#### step1:

View and remove hive kernel
```
jupyter kernelspec list
jupyter kernelspec remove hive
```

#### step2:
uninstall hive kernel:

```
pip uninstall hive-kernel
```

ALL DONE! 🎉🎉🎉

## Using

```
jupyter notebook
```
<img src="image/hive2.png" width = "700" height = "300" />

### step1: you should set hive server (host and port)

### step2: write your hive sql
![](image/hive1.png)

## Quote 
kernel logo

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Apache_Hive_logo.svg/300px-Apache_Hive_logo.svg.png" width = "32" height = "32" />

- https://en.wikipedia.org/wiki/Apache_Hive
