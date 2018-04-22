#!/usr/bin/env bash
virtualenv -p python env
source ./env/bin/activate
pip install -r requirements.txt
