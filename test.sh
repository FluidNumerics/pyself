#!/bin/bash

pip3 install . --user --upgrade

for f in examples/*.py;
do
  python3 $f
done
