#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run python monitoring.py &
sleep 15
if [ $? -eq 0 ]; then exit 0; else exit $?; fi
