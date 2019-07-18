init:
	pip install -r requirements.txt --user
	sudo apt install mecab
	sudo apt install libmecab-dev
	sudo apt install mecab-ipadic-utf8

test:
	nosetests tests
