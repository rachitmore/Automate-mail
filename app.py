import logging
from flask import Flask,request,render_template
from flask_cors import CORS, cross_origin
from mailsender import automail
import time
import PyPDF2

logging.basicConfig(filename="application.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

mail_sender = automail()

app =Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST']) # To render Homepage       
def upload_file():
   return render_template('upload.html')

@app.route('/mail', methods=['POST',"GET"])
@cross_origin()
def mailsender():
    if (request.method=='POST'):
        email_Id = request.form["Email Id"]
        password = request.form["Password"]
        
        f = request.files["Email Id file"]

        subject = request.form['Subject']
        body = request.form['Body']
        a = request.files["Attachment file"]

        f.save(f.filename)
        
        logging.info("File Received from website")

        f = open("doc1.pdf","rb")
        pdfReader = PyPDF2.PdfReader(f)
        pageObj = pdfReader.pages[0]
        mail_read = pageObj.extract_text()

        logging.info("File read")
  
        list_mail = mail_read.split()
       
        logging.info("File list has been created")

        for i in list_mail:
            mail_sender.autosender(i,subject,body,email_Id,password,a)
                
        logging.info("Email Sent")
        result = "Email sent successfully"


        return render_template("upload.html",result = result)

if __name__ == "__main__":
   app.run(debug=True)
   app.run(host='0.0.0.0', port=5000)
