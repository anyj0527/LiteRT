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
"""LiteRT is for mobile and embedded devices.

LiteRT is the official solution for running machine learning models on mobile
and embedded devices. It enables on-device machine learning inference with low
latency and a small binary size on Android, iOS, and other operating systems.
"""

import os

from setuptools import find_packages
from setuptools import setup
PACKAGE_NAME = os.environ['PROJECT_NAME']
PACKAGE_VERSION = os.environ['PACKAGE_VERSION']
DOCLINES = __doc__.split('\n')

setup(
    name=PACKAGE_NAME.replace('_', '-'),
    version=PACKAGE_VERSION,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    url='https://www.tensorflow.org/lite/',
    author='Google AI Edge Authors',
    author_email='packages@tensorflow.org',
    license='Apache 2.0',
    include_package_data=True,
    has_ext_modules=lambda: True,
    keywords='litert tflite tensorflow tensor machine learning',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=[]),
    package_dir={'': '.'},
    package_data={'': ['*.so', '*.pyd']},
    install_requires=[
        'numpy >= 1.23.2',  # Better to keep sync with both TF ci_build
        # and OpenCV-Python requirement.
    ],
)
