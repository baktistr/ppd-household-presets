.PHONY: setup notebooks lab

setup:          ## create .venv with the dependencies
	uv sync

notebooks:      ## run every notebook in order: builds data/ and runs the checks inside them
	cd notebooks && ../.venv/bin/jupyter nbconvert --to notebook --execute --inplace 0*.ipynb

lab:            ## open the notebooks
	.venv/bin/jupyter lab notebooks/
