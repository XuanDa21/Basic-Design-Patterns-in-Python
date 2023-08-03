#!/bin/bash
for python_file_name in $(find /root/python/Design-Pattern-py -name *.py)
do
   python3 $python_file_name
done