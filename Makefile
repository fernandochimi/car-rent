doc:
		$(MAKE) -C docs/ html
		open docs/_build/html/index.html

test:
		coverage run --source="car_rent/car_rent" --omit="../../**migrations**, ../../**tests**" ./car_rent/manage.py test car_rent -v 2 --settings=settings.test --failfast
		coverage report -m

html:
		coverage html
		# open htmlcov/index.html
		xdg-open htmlcov/index.html

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log