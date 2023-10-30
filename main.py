from flask import Flask , render_template, send_file
from chess_opening_generator import random_opening_generator


app = Flask(__name__ , template_folder='templates')





@app.route('/')
def index():
	'''
    # Call the random_opening_generator function to generate and save the image
    image_filename = random_opening_generator()
    return render_template('index.html', image_filename=image_filename)
	'''
	eco, name, moves = random_opening_generator()

	return render_template("index.html",opening_name=name, eco = eco , moves = moves)

@app.route('/image/<filename>')
def image(filename):
    # Serve the image from the static directory
    return send_file(f'static/{filename}')


if __name__ == '__main__':
    app.run(debug=True)