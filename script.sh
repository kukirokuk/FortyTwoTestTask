#!/bin/bash
# stderr to file

python manage.py modelcount 2> `date +"%m_%d_%Y"`.dat