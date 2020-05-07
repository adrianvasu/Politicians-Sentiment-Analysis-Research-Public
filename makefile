# Run method to invoke this use make run
run:
	python3 FinalProjectController.py

# Clean method to remove garbage files and setup for another run
# to invoke this use make clean
clean:
	rm -rf *.csv
	rm -rf __pycache__/
	
