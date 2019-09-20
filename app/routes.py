from app import app
from flask import render_template, request, url_for
from app.forms import InputTextForm
from .text_analyser import TextAnalyser
import json

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/textminer', methods=('GET', 'POST'))
def textminer():
    input_text_form = InputTextForm()
    if input_text_form.validate_on_submit():
        userText = input_text_form.inputText.data
        myText = TextAnalyser(userText, 'EN')
        myText.preprocessText(lowercase = input_text_form.ignoreCase.data,
                    removeStopWords = input_text_form.ignoreStopWords.data)
        commonWords = myText.getMostCommonWords(10)
        commonWords.insert(0, ('Common Word', 'Frequency'))
        data = [list(elem) for elem in commonWords]
        return render_template('textminer.html',
                        form = input_text_form,
                        numChars = myText.length(),
                        numTokens = myText.getTokens(),
                        uniqueTokens =myText.uniqueTokens(),
                        data = data,
                        miningComplete = True)
    return render_template('textminer.html', form = input_text_form, miningComplete = False)
