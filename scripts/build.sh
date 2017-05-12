#!/bin/bash

set -e
set -o pipefail

cd "$(dirname "$0")"/..
mkdir -p build/wheel

python setup.py bdist_wheel --dist-dir ../build/wheel
