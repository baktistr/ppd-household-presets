.PHONY: setup corpus notebooks test

setup:          ## create .venv with the dependencies
	uv sync

corpus:         ## refresh data/corpus/flows.csv from ../ppd-preference-app
	.venv/bin/python scripts/import_corpus.py

notebooks:      ## run every notebook in order (writes data/)
	cd notebooks && ../.venv/bin/jupyter nbconvert --to notebook --execute --inplace 0*.ipynb

test:
	.venv/bin/python -m pytest -q
