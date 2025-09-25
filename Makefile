.PHONY: install virtualenv ipython test watch lint
install:
	@.venv/bin/python3 -m pip install -e .[dev]

virtualenv:
	@.venv/bin/python3 -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

test:
	@.venv/bin/pytest -vv -s

watch:
	# @.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
