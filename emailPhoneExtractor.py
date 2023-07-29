#! python3
import re, pyperclip
#Phone number Regex
phoneRegex = re.compile(r'''
(
((\+ | 00)\s*(216) | \((\+ | 00)\s*216\))? #Tunisian Code +216
\s?\d+\s?\d+\s?\d+\s?\d+\s?\d+\s?\d+\s?\d+\s?\d+#The rest of the 8 digit phone number. Each digit could have any number of space before and/or after it.
)
''', re.VERBOSE)
#TEmail Regex
emailRegex = re.compile(r'''
[a-zA-Z0-9._+]+ #First part
@ #@
[a-zA-Z0-9._+]+ #Domaine name

''', re.VERBOSE)
#Get the text from the clipboard
text = pyperclip.paste()

#Extract email and phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

phoneNumbers = []


for number in extractedPhone:
    #Remove newline character from the phone number
    spacelessNumber = number[0].replace('\n', '')
    phoneNumbers.append(spacelessNumber)


#Copy extracted emails and numbers (after formatting them) to the clipboard
results = "Phone numbers: \n" + "\n".join(phoneNumbers) + "\n\nEmail adresses: \n" + "\n".join(extractedEmail)
print(results)
pyperclip.copy(results)
