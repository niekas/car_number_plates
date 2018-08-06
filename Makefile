build_and_run:
	npm run build
	cp plates/plates/build/static/css/*.css plates/plates/static/css/
	cp plates/plates/build/static/js/*.js plates/plates/static/js/
	cp plates/plates/build/index.html plates/plates/templates/index.html
	./plates/manage.py runserver 8000

test:
	./plates/manage.py test plates.tests
