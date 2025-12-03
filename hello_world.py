from flask import Flask

app = Flask(__name__)


def generate_html(message):
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="540" width="1200" src="https://i0.wp.com/build5nines.com/wp-content/uploads/2023/02/GitHub_Actions_Featured_Image.jpg">
                <br>
                {0}<br>
            </div>
        </body>
        </html>""".format(message)
    return html


def greet():
    return "Hello World from Flask CI/CD Lab!"


@app.route('/')
def hello():
    return generate_html(greet())


@app.route('/greeting')
def greeting():
    return greet()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4049)
