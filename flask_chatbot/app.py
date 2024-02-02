from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)


@app.route("/")  # root URL; when URL is first loaded
def index():
    global text  # makes global text variable to pull from URL in next line
    text = request.args.get('text')
    return render_template("chat.html")


@app.route("/get", methods=['GET', 'POST'])  # whenever text message is sent
def chat():
    msg = request.form["msg"]
    input = msg
    return get_chat_response(input, None)


def get_chat_response(input, context):
    qa_model = pipeline("question-answering",
                        "timpal0l/mdeberta-v3-base-squad2")
    context = text
    ans, score = qa_model(question=input, context=context)[
        'answer'], qa_model(question=input, context=context)['score']
    return ans + " " + str(score)


if __name__ == '__main__':
    app.run()
