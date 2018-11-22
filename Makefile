all: install migrate webpack collectstatic

install:
	@npm install
	@pip install -Ur requirements/base.txt

webpack:
	@webpack --display-error-details

collectstatic:
	@python ./manage.py collectstatic --noinput

loaddata:
	@python ./manage.py loaddata $(FIXTURES)

migrate:
	@python ./manage.py migrate
