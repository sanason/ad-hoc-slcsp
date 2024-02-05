# Overview

The script `slcsp.py` is a solution to the problem described [here](./input/README.md). The problem comes from
[Ad Hoc](https://homework.adhoc.team/slcsp/). Everything in the `input` directory comes from the "Included files" zip
on that Ad Hoc page. All other files are my own.

# How to run

## Running the script

The script is written in Python3 and only requires the standard library. 

Assuming you have Python3 installed, the command to run the script is:
```shell
python3 slcsp.py
```

The script reads from input files in `./input` and writes its output to stdout (as described in the problem statement).

## Running the tests

There are a few unit tests for the script in `test_slcsp.py`. They are meant to be run with pytest. 

Assuming you have pipenv installed, the command to run the tests is:
```shell
pipenv run pytest
```