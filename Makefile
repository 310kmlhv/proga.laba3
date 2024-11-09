all: main

main:
	python3 main.py

test:
	python3 -m unittest test.py

rebuild: clean main

clean:
	rm -rf *.txt test
