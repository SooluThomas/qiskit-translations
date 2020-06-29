#!/bin/bash

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Script for publishing production the translated documentation.

# Non-travis variables used by this script.
SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit.git"
TARGET_REPOSITORY="git@github.com:SooluThomas/qiskit-translations.git"
TARGET_DOC_DIR="documentation/"
SOURCE_DOC_DIR="docs/_build/html/"
SOURCE_DIR=`pwd`
TARGET_BRANCH="gh-pages"

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

# Clone the sources files and po files to $SOURCE_DIR/docs_source
git clone --depth=1 $SOURCE_REPOSITORY docs_source
rclone sync -v --exclude='locale/**' docs_source/docs docs

pushd $SOURCE_DIR/docs

# Make translated document
sphinx-build -b html -j auto -D content_prefix=documentation -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

git clone https://SooluThomas:$REPO_TOKEN@github.com/SooluThomas/qiskit-translations.git --branch=gh-pages gh-pages

echo "Make directory locale/"
mkdir -p $TARGET_DOC_DIR
echo "made directory"

echo "List files"
ls

echo "copy html files to locale/"
cp -r $SOURCE_DIR/$SOURCE_DOC_DIR/* gh-pages/$TARGET_DOC_DIR/

cd gh-pages
ls

git remote set-url origin https://SooluThomas:$REPO-TOKEN@github.com/SooluThomas/qiskit-translations.git

git config user.name "SooluThomas"
git config user.email "soolu.elto@gmail.com"

echo "git add"
git add $TARGET_DOC_DIR

# Commit and push the changes.
git commit -m "Automated documentation update from meta-qiskit"
git push --quiet origin $TARGET_BRANCH

popd
