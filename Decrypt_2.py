import re
def decrypt(string):

    newstr=re.findall('[0-9]{2}[#]|[0-9]{1}',string)
    form=''
    for i in newstr:
        if(len(i)==3):
           form+=chr(97+int(i[0:2])-1)
        else:
           form+=chr(97+int(i[0])-1)
    return form


string='12#123410#11#1#'
print(decrypt(string))