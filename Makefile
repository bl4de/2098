## Installation
install:
	python3 -m pip install -r requirements.txt

## Cleanup
cleanup:
	rm -rf ./src/game/__pycache__
	rm -rf ./src/utils/__pycache__
	
## Run 2098
run:
	python3 ./main.py

