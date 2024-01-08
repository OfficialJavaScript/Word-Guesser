#!/usr/bin/env python3

# Problems: If you have the word ferry, and you enter fewer, it will show that you have e correctly after the F, but the e at the second r will say its correct but in the wrong place.

from flask import Flask, render_template, request, redirect
from wordgen import generate_word
from word_check import word_check

app = Flask(__name__)

word = ""
word_length = 5
current_word = 1
first_time = True
won = False
error = False
answered_rows = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
correct_rows = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
to_be_sent = ['', '', '', '', '']
crto_be_sent = ['', '', '', '', '']

@app.route("/", methods=['GET'])
def main():
    global word, first_time, error
    if first_time == True:
        error = False
        word = generate_word(word_length)
        first_time = False
    return render_template("index.html", word=word, answered_rows=answered_rows, current_word=current_word, correct_rows=correct_rows, won=won, error=error)

@app.route("/check_word", methods=['POST'])
def check_word():
    global to_be_sent, word_length, word, current_word, won, error
    if current_word == 1:
        for i in range(1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("a{}".format(i))
    elif current_word == 2:
        for i in range (1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("b{}".format(i))
    elif current_word == 3:
        for i in range (1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("c{}".format(i))
    elif current_word == 4:
        for i in range (1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("d{}".format(i))
    elif current_word == 5:
        for i in range (1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("e{}".format(i))
    elif current_word == 6:
        for i in range (1, word_length + 1):
            to_be_sent[i - 1] = request.form.get("f{}".format(i))
            
    results = word_check(word, to_be_sent, correct_rows, current_word - 1)
    if results == "error":
        error = True
        return redirect("/")
    answered_rows[current_word - 1][0] = to_be_sent[0]
    answered_rows[current_word - 1][1] = to_be_sent[1]
    answered_rows[current_word - 1][2] = to_be_sent[2]
    answered_rows[current_word - 1][3] = to_be_sent[3]
    answered_rows[current_word - 1][4] = to_be_sent[4]
    print(word)
    if correct_rows[current_word - 1][0] == "cr" and correct_rows[current_word - 1][1] == "cr" and correct_rows[current_word - 1][2] == "cr" and correct_rows[current_word - 1][3] == "cr" and correct_rows[current_word - 1][4] == "cr":
        won = True
        current_word = 0
        return redirect('/')
    current_word += 1
    return redirect('/')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=80, debug=True)