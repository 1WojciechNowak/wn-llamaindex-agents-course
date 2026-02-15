.PHONY: help install clean kernel jupyter

help:
	@echo "======================================"
	@echo "# Llamaindex Agents Course 🦙🤖"
	@echo "======================================"
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "Setup"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Remove virtual environment"
	@echo ""
	@echo "Jupyter"
	@echo "  make kernel    - Register Jupyter kernel"
	@echo "  make jupyter   - Launch Jupyter Notebook"



# -----------------------------------------
# Setup
# -----------------------------------------

install:
	poetry install

clean:
	poetry env remove python || true

# -----------------------------------------
# Jupyter
# -----------------------------------------

kernel:
	poetry run python -m ipykernel install --user --name=wn-llamaindex-agents-course --display-name "Python (wn-llamaindex-agents-coure)"

jupyter:
	poetry run jupyter notebook
