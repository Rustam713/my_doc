


from flask import Flask, request, render_template


app = Flask(__name__)

data = {
    {'name': 'Index', 'url': '/'},
    {'name': 'About', 'url': '/about'},
    {'name': 'Contact', 'url': '/contact'}
}

@app.route('/contact')
def contact():
    return render_template('contact.html', data=data)

@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html', data=data)


if __name__ == 'main':
    app.run(debug=True)
