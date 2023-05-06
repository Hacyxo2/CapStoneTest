
from flask import Flask, request, Response, g, make_response
from flask.templating import render_template
from . import deepLearning

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html', name='PyCharm')


@app.route('/nst_get')
def dlt_get():
    return render_template('nst_get.html')


@app.route('/nst_post', methods=['GET', 'POST'])
def nst_post():
    if request.method == 'POST':
        refer_img = request.form['refer_img']
        refer_img_path = '/images/nst_get/'+str(refer_img)

        user_img = request.files['user_img']
        user_img.save('D:/develop/Flask/flaskProject/static/images/'+str(user_img.filename))
        user_img_path = '/images/'+str(user_img.filename)

        transfer_img = deepLearning.main(refer_img_path, user_img_path)
        transfer_img_path = '/images/'+str(transfer_img.split('/')[-1])

    return render_template('nst_post.html',
                           refer_img=refer_img_path, user_img=user_img_path, transfer_img=transfer_img_path)


if __name__ == '__main__':
    app.run()
