from connection import app

@app.route('/')
def index():
	return "Hello word!"

if __name__ == '__main__':
	app.run(debug=True)