# Multi command executor

Execute identical command to the specified directory (multi-threaded)

---

1. [Environment](#environment)
1. [Available commands](#available-commands)
1. [Usage](#usage)

---

## Environment

- Arch Linux x86_64 (2019/10/24)
- Python 3.7.4
- jpegoptim 1.4.6
- OptiPNG 0.7.7

## Available commands

- Jpegoptim ([Windows](https://sourceforge.net/projects/jpegoptim/files/), [Linux](https://www.kokkonen.net/tjko/projects.html))
- [OptiPNG](http://optipng.sourceforge.net/)

## Usage

- You can add these scripts to your `PATH` environment variable
- Your stdout should be messed up with threaded executing commands

```
# multi_jpegoptim.py & multi_optipng.py
$ python multi_jpegoptim.py /path/to/images/
```
