#!/bin/bash

set -ex

docker build -t cbata/hello-katib-quadratic-function .

docker run -it --rm cbata/hello-katib-quadratic-function python main.py --x1 -1 --x2 3.5

docker push cbata/hello-katib-quadratic-function