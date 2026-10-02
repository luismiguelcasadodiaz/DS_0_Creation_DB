# Set the default goal so running `make` with no arguments prints the help menu

.DEFAULT_GOAL := help
environment := piscine
DEF_TAB_DS0_EX02 ?=DS_0_Creation_DB/data/customer/data_2022_oct.csv 

.PHONY: help
help: ## Show this help menu
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
# ###############################################################33
.PHONY: DS0_ex02
DS0_ex02: ## import one table (DEF_TAB_DS0_EX02=DS_0_Creation_DB/data/customer/data_2022_oct.csv )
	python DS_0_Creation_DB/ex02/table.py $(DEF_TAB_DS0_EX02)

.PHONY: DS0_ex03
DS0_ex03: ## import files from folder
	python DS_0_Creation_DB/ex03/automatic_table.py DS_0_Creation_DB/data/customer 

.PHONY: DS0_ex04
DS0_ex04: ## import items
	python DS_0_Creation_DB/ex04/items_table.py DS_0_Creation_DB/data/item/item.csv 
# ###############################################################33

.PHONY: set
set: ## Set a python environment for this project
	bash -c "python3 -m venv $(environment) && source $(environment)/bin/activate && pip install --upgrade pip &&pip install -r requirements.txt"

.PHONY: activate
activate: ## Activate the python environment for this project
	@echo "Run: source $(environment)/bin/activate"

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
	cp ex02/table.py ../../DS0/ex02
	cp ex03/automatic_table.py ../../DS0/ex03
	cp ex04/items_table.py ../../DS0/ex04

