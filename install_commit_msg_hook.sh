#!/bin/bash

HOME_DIR=`pwd`
HOOKS_DIR="$HOME_DIR/.git/hooks"

cp -f $HOME_DIR/commit-msg.py $HOOKS_DIR/commit-msg

chmod +x $HOOKS_DIR/commit-msg