import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']

        # Phone number Regex
        phoneRegex = re.compile(r'''
        (
        (\+216 | 00 216 | \(\+216\))? #Tunisian Code +216
        \s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d
        )
        ''', re.VERBOSE)
        
        # Email Regex
        emailRegex = re.compile(r'''
        [a-zA-Z0-9._+]+ #First part
        @ #@
        [a-zA-Z0-9._+]+ #Domain name
        ''', re.VERBOSE)
        
        # Extract email and phone from the text
        extractedPhone = phoneRegex.findall(user_text)
        extractedEmail = emailRegex.findall(user_text)

        phoneNumbers = []

        for number in extractedPhone:
            # Remove newline character from the phone number
            spacelessNumber = number[0].replace('\n', '')
            phoneNumbers.append(spacelessNumber)

        # Format the results
        results = {
            "resultPhoneNumber": "\n".join(phoneNumbers),
            "resultEmailAdress": "\n".join(extractedEmail)
        }

        return render_template('index.html', **results)

    return render_template('index.html', resultPhoneNumber=None, resultEmailAdress=None)

if __name__ == '__main__':
    app.run(debug=True)
