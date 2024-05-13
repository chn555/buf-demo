#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate

pip install betterproto==v2.0.0b6
pip install protobuf~=5.26
pip install setuptools_scm>=8

deactivate

buf generate