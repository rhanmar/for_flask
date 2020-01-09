from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)
'''
@app.route('/')
def hello_world():
	return 'hi!'
'''
@app.route('/test22')
def test():
	return 'test!'

@app.route('/user/<username>')
def show_username(username):
	return username

@app.route('/id/<int:post_id>')
def show_post_id(post_id):
	return str(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return subpath



@app.route('/')
@app.route('/main.html')
def main():
	return render_template(
		'index.html',
		title="My Title!",
		header='just header',
		text='some text'
		)



@app.route('/posts', defaults={'page': 1})
@app.route('/posts/<int:page>')
def list_posts(page):
	return str(page)


@app.route('/new/<key>')
@app.route('/old/<key>', redirect_to='/new/<key>')
def redir(key):
	return str(key)

@app.route('/test_url_for')
def test_url_for():
	return url_for('test') # /test22
	
@app.route('/count/<int:number>')
def count(number):
	return render_template(
		'counting.html', 
		title='counting',
		number=number
		)

@app.route('/echo/')
def echo():
	print(request.path)
	print('!!')
	print(request.data)
	return request.data

@app.route('/test_get', methods=['GET'])
def get_something():
	return "GET"

'''
@app.route('/test_post', methods=['POST'])
def post_something():
	return "POST"
'''

@app.route('/args')
def show_query():
	result  = {}
	for key in request.args.keys():
		result[key] = request.args.getlist('{}'. format(key))
	return render_template('args.html', args=result)

@app.route('/not_found/')
def not_found():
	return 'not_found', 404 # http response is 404

@app.errorhandler(404)
def not_found(error):
	return "Code is 404, error is {}".format(error)

@app.route('/foo')
def foo():
	response = make_response('foo')
	response.headers['test'] = 'test_test' # header
	response.mimetype = 'text/plain' # type of content
	response.status_code = 418 # status
	response.set_cookie('foo', 'bar')
	print('!!')
	print(response)
	print(response.headers)
	print(response.status_code)
	return response


@app.route('/make_error')
def make_error():
	n1 = 1
	n2 = 0
	return n1 / n2