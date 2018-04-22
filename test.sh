#!/usr/bin/env bash
source ./env/bin/activate
nosetests --nocapture --verbosity=2 app
