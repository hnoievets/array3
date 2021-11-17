#!/bin/bash

if [ -d venv ]
  source venv/bin/activate
  python3 main.py
else
  python3 -m venv venv
  source venv/bin/activate
  python3 main.py
fi

exit 1