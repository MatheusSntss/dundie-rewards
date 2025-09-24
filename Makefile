.PHONY: install virtualenv ipython test watch
install:
	@.venv/bin/python3 -m pip install -e .[dev]

virtualenv:
	@.venv/bin/python3 -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s

testci:
	@.venv/bin/pytest -v --junitxml=test-result.xml

watch:
	# @.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
