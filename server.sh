#!/usr/bin/env bash

./venv/bin/gunicorn -k gevent server:app -D