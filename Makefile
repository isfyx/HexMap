install_dev:
	pip install -e .

clean:
	rm -rf build dist
	rm -rf src/hexmap/__pycache__
	rm -rf src/hexmap_isfyx.egg-info