.PHONY: install virtualenv ipython test watch lint fmt
install:
	@.venv/bin/python3 -m pip install -e .

virtualenv:
	@.venv/bin/python3 -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -s --forked

watch:
	# @.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
