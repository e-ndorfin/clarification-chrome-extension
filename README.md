# Quiz me!

Quiz me! is an Chrome extension which allows user to ask questions about selected text. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules from requirements.txt.

```bash
pip install -r requirements.txt
```

Then install the Chrome extension. 
1. Download this repo as a [ZIP file from GitHub](https://github.com/e-ndorfin/quiz-me/archive/refs/heads/main.zip).
2. Unzip the file and find the quiz-me-extension folder. 
3. In Chrome go to the extensions page ([chrome://extensions](chrome://extensions)).
4. Enable Developer Mode.
5. Drag the quiz-me-extension folder anywhere on the page to import it (do not delete the folder afterwards).

## Usage

Run the Flask app. 
```bash
python flask_chatbot/app.py 
```
Then highlight text on any website, right click, and click on the Quiz me! option. You can then ask the chatbot questions about the content. 
