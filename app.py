from flask import Flask, render_template, request, jsonify
import warnings
import spacy
# Import the function from the module where it is defined
from new import retrieve_answer_from_pdf

nlp = spacy.load("en_core_web_sm")

warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/create_knowledgebase", methods=["POST"])
def create_knowledgebase():
    # Assuming create_vector_db() is a function that initializes your knowledge base
    return jsonify({"status": "Knowledge base created"}), 200

@app.route("/get", methods=["POST"])
# def chat():
#     msg = request.form["msg"]
#     # Call the retrieve_answer_from_pdf function with the path to your PDF and the message from the user
#     response = retrieve_answer_from_pdf("data1.pdf", msg)
#     return jsonify({"result": response})

def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_text = " ".join([token.lemma_ for token in doc])
    return lemmatized_text

def complaint():
    print("Handling complaint...")

def get_Chat_response(text):
    lemmatized_text = lemmatize_text(text)
    if "register a complaint" in lemmatized_text or "register my complaint" in lemmatized_text:
        complaint()
        return "Complaint process initiated."
    else:
        response = retrieve_answer_from_pdf(r"E:\AI bot\AmazonChat\data1.pdf", lemmatized_text)
        return response

if __name__ == '__main__':
    app.run(debug=True)
