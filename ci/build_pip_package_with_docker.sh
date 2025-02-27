#!/usr/bin/env bash
# Copyright 2024 The AI Edge LiteRT Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
set -ex

DOCKER_PYTHON_VERSION="${DOCKER_PYTHON_VERSION:-3.11}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d /third_party_tensorflow ]; then
  # Running on host.
  cd ${SCRIPT_DIR}
  docker build . -t tflite-builder -f tflite-py${DOCKER_PYTHON_VERSION}.Dockerfile

  docker run -v ${SCRIPT_DIR}/../third_party/tensorflow:/third_party_tensorflow \
    -v ${SCRIPT_DIR}:/script_dir \
    -e NIGHTLY_RELEASE_DATE=${NIGHTLY_RELEASE_DATE} \
    --entrypoint /script_dir/build_pip_package_with_docker.sh tflite-builder
  exit 0
else
  # Running inside docker container
  cd /third_party_tensorflow

  # Run configure.
  configs=(
    '/usr/bin/python3'
    '/usr/lib/python3/dist-packages'
    'N'
    'N'
    'Y'
    '/usr/lib/llvm-18/bin/clang'
    '-Wno-sign-compare -Wno-c++20-designator -Wno-gnu-inline-cpp-without-extern'
    'N'
  )
  printf '%s\n' "${configs[@]}" | ./configure

  bash /script_dir/build_pip_package_with_bazel.sh
fi
