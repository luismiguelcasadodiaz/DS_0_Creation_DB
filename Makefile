# Set the default goal so running `make` with no arguments prints the help menu

.DEFAULT_GOAL := help
environment := DS0
DEF_TAB_DS0_EX02 ?=~/ds/DS_0_Creation_DB/data/customer/data_2022_oct.csv 
DEF_DIR_DS0_EX03 ?=~/ds/DS_0_Creation_DB/data/customer
DEF_TAB_DS0_EX04 ?=~/ds/DS_0_Creation_DB/data/item/item.csv

.PHONY: help
help: ## Show this help menu
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
# ###############################################################33
.PHONY: DS0_ex02
DS0_ex02: ## import one table (DEF_TAB_DS0_EX02=~/ds/DS_0_Creation_DB/data/customer/data_2022_oct.csv )
	python ex02/table.py $(DEF_TAB_DS0_EX02)

.PHONY: DS0_ex03
DS0_ex03: ## import files from folder (DEF_DIR_DS0_EX03 ?=~/ds/DS_0_Creation_DB/data/customer )
	python ex03/automatic_table.py $(DEF_DIR_DS0_EX03)

.PHONY: DS0_ex04
DS0_ex04: ## import items DEF_TAB_DS0_EX04 ?=~/ds/DS_0_Creation_DB/data/item/item.csv
	python ex04/items_table.py $(DEF_TAB_DS0_EX04)
# ###############################################################33

.PHONY: set
set: ## Set a python environment for this project
	sh -c "python3 -m venv $(environment) && source $(environment)/bin/activate && pip install --upgrade pip &&pip install -r requirements.txt"

.PHONY: activate
activate: ## Activate the python environment for this project
	@echo "Run: source ../$(environment)/bin/activate"

.PHONY: deactivate
deactivate: ## Deactivate the python environment for this project
	deactivate

.PHONY: unset
unset: ## removes the python 
	rm -rf $(environment)

.PHONY: upgrade
upgrade: ## Upgrades pip
	pip install --upgrade pip

.PHONY: norminette
norminette: ## Run norminette on all .py files
	flake8  */*.py		

.PHONY: entrega
entrega: ## copies deliverable files to 42 repo
	mkdir ../../DS0/ex00
	mkdir ../../DS0/ex02
	mkdir ../../DS0/ex03
	mkdir ../../DS0/ex04
	cp ex00/VM-instructions.md ../../DS0/ex00/
	cp ex02/table.py ../../DS0/ex02/
	cp ex03/automatic_table.py ../../DS0/ex03/
	cp ex04/items_table.py ../../DS0/ex04/
	cp Makefile ../../DS0
	cp requirements.txt ../../DS0

.PHONY: drop
drop: ## Drops items and data_202*_*** tables
	psql -U luicasad -d piscineds -h localhost -c "DROP TABLE IF EXISTS data_2022_oct; DROP TABLE IF EXISTS data_2022_nov; DROP TABLE IF EXISTS data_2022_dec; DROP TABLE IF EXISTS data_2023_jan; DROP TABLE IF EXISTS items;"

