start:
	export FLASK_APP=hello_world.py && \
	export FLASK_ENV=development && \
	python -m flask run

# for gunicorn:
# gunicorn --workers=4 --bind=127.0.0.1:5000 hello_world:app
