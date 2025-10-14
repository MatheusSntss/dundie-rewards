.PHONY: install virtualenv ipython test watch lint fmt clean build
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

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*__pycache__'  -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs_build


build: 
	python setup.py sdist bdist_wheel



