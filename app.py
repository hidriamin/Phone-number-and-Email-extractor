from flask import Flask, render_template, request
app = Flask(__name__)
import re


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #Phone number regex
        phoneRegex = re.compile(r"""(
        (\+\s?216 | 00\s?216 | \(\+\s?216\) | \(00\s?216\))? #Tunisian country code
        \s?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-?\d\s?-? #number
        )""",re.VERBOSE)
        #Email regex
        emailRegex = re.compile(r"""[a-zA-Z0-9]+ #first part
        @ #@
        [a-zA-Z0-9.\-]+ #domain name(first part)
        \. #dot
        [a-zA-Z0-9.\-]{2,3} #domain name last part (exemple: .com .net)""", re.VERBOSE)
        
        #get the user text
        text = request.form["user_text"]
        
        #match the phone number and email regex
        phoneNumberMatch = phoneRegex.findall(text)
        emailAdresses = emailRegex.findall(text)
        
        #only use the first item in each tuple because it's the full number 
        phoneNumbers = []
        for num in phoneNumberMatch:
            phoneNumbers.append(num[0])
            
        
        #format the list
        phoneNumberList = "\n".join(phoneNumbers)
        emailList = ",\n".join(emailAdresses)
        
        return render_template("index.html",phoneNumberList=phoneNumberList, emailList=emailList)
    
    return render_template("index.html",phoneNumberList="",emailList="")


   
if __name__ == "__main__":
    app.run(debug=True)           