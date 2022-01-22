#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:58:03 2022

@author: aihub
"""

import os
os.system("sudo apt update;sudo snap install multipass")
os.system("multipass launch --name foo;multipass exec foo -- lsb_release -a;multipass launch -n bar --cloud-init cloud-config.yaml")
os.system("multipass list;multipass stop foo bar;multipass start foo")
