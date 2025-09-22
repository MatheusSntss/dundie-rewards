.PHONY: install virtualenv ipython
install:
	@.venv/bin/python3 -m pip install -e .[dev]

virtualenv:
	@.venv/bin/python3 -m venv .venv

ipython:
	@.venv/bin/ipython
