from app import app
from flask import render_template, request, url_for
from app.forms import InputTextForm
from .text_analyser import TextAnalyser

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/textminer', methods=['GET', 'POST'])
def textminer():
    if request.method == 'GET':
        input_text_form = InputTextForm()
        return render_template('textminer.html', form = input_text_form, miningComplete = False)
    elif request.method == 'POST':
        input_text_form = InputTextForm(request.POST)
        if input_text_form.validate_on_submit():
            userText = input_text_form.inputText.data
            myText = TextAnalyser(userText, 'EN')
            myText.preprocessText(lowercase = input_text_form.ignoreCase.data,
                        removeStopWords = input_text_form.ignoreStopWords.data)
            return render_template('textminer.html',
                         numChars = myText.length(),
                         numTokens = myText.getTokens(),
                         uniqueTokens =myText.uniqueTokens(),
                         commonWords = myText.getMostCommonWords(10),
                         miningComplete = True)

