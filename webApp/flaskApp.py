from flask import Flask, request, render_template, redirect, flash, Response, send_from_directory
import flask
import os
app = Flask(__name__)


def simplifyFile(fileName):
    file = open(fileName, 'r+')
    text = [file.read()]
    outputText = []
    flag = 0
    start = 0
    for i in text[0]:
        if start == 0 and i == '\n':
            continue
        if flag == 1:
            flag = 0
            if i == '\n':
                outputText.append('\n\n')
                continue
            else:
                outputText.append('\\N')
        if i == '.':
            start = 1
            outputText.append(' \\F')
        elif i == '\n':
            start = 1
            flag = 1
        else:
            start = 1
            outputText.append(i)
    file.seek(0)
    file.writelines(outputText)
    file.close()
    return


@app.route('/download')
def download():
    return render_template('download.html')


@app.route('/download', methods=['POST'])
def downloadFiles():
    fileName = request.form['annotationNumber']
    fileName = 'Annotation' + fileName + '.txt'
    uploads = os.path.join(flask.current_app.root_path)
    return send_from_directory(directory=uploads, filename=fileName, as_attachment=True)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    fileName = request.form['annotationNumber']
    fileName = 'Annotation' + fileName + '.txt'
    originalText = request.form['originalText']
    simplifiedText = request.form['simplifiedText']
    if request.method == 'POST':
        with open(fileName, 'a') as f:
            f.write('\n\nOriginal:\n\n')
            f.write(str(originalText))
            f.write('\n\nSimplified:\n\n')
            f.write(str(simplifiedText))
    simplifyFile(fileName)
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
