test:
		py.test -s tests
.PHONY: test

build: clean
		python setup.py sdist
.PHONY: build

clean:
		rm -rf dist build *.egg-info .cache tests/__pycache__
.PHONY: clean

upload:
		make clean
		make build
		devpi upload dist/*
		pip uninstall saturn-fs
.PHONY: upload

rpm: build
	mkdir -p scripts/rpm/build/tmp/saturn-fs && \cp -f dist/*.tar.gz scripts/rpm/build/tmp/saturn-fs
	cd scripts/rpm && mkdir -p rpms && python build_rpm.py
.PHONY: rpm
