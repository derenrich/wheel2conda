#!/bin/bash

set -e
set -o pipefail

cd "$(dirname "$0")"/..

# assume there is only one
WHEEL_FILENAME=`ls build/wheel/*whl`
WHEEL_FILENAME=`basename $WHEEL_FILENAME`

PUBLISH_URL="https://publish.artifactory.palantir.build/artifactory/internal-python-release/deltasierra/wheel2conda/$WHEEL_FILENAME"


curl -u $ARTIFACTORY_USERNAME:$ARTIFACTORY_PASSWORD -T "build/wheel/$WHEEL_FILENAME" $PUBLISH_URL
