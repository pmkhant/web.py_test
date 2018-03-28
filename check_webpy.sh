#!/bin/bash

python webpy.py > /dev/null &
nosetests --with-coverage

