from just_stats import app


@app.route('/')
def index():
	return "HELLO WORLD"