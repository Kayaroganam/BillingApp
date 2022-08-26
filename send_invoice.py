from database_operation import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from variables import var

sender_email = var.My_Email
sender_password = var.My_Email_Password

#Make the content ready to send as html
def make_html():

    result = select_all_selected()
    total__ = total_price()
    list__ = []

    for i in result:
        temp = f"""
        <tr>
            <td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">{i[0]}</td>
            <td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">{i[3]}</td>
            <td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">{i[4]}</td>
            <td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">{i[5]}</td>
        </tr>
        """

        list__.append(temp)

    __list = "".join(list__)

    html = f'''
    <html>
    <head>
    </head>
    <body style="font-family: 'Courier New', Courier, monospace;">
        <h1 style="font-family: sans-serif; color: tomato;">INVOICE</h1>
        <table style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">
            <tr>
                <th style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">S.no</th>
                <th style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">Item name</th>
                <th style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">Qty</th>
                <th style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">Price</th>
            </tr>
            {__list}
            <tr>
            <td td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;"></td>
            <td td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">Thank you for your business!</td>
            <td td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">Total</td>
            <td td style="border-top: 1px solid #CE2232;border-right: 1px solid #219E4A;border-bottom: 1px solid #0974B0;border-left: 1px solid #FFE004;border-collapse: collapse;text-align: center;padding-right: 40px;padding-left: 40px;">₹{total__}</td>
            </tr>
        </table>
        <p>If you have any questions about this invoice,<br> please contact <a href="#">{sender_email}</a> </p>
        
    </body>
    </html>
    '''

    return html


#this funtion will send an email to give email attribute
def send_mail(receiver_email):
    
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "INVOICE"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    html = make_html()

    part = MIMEText(html, "html")

    msg.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print("Mail sent successfully.")



if __name__ == "__main__":
    
    send_mail("iamkayarogan@gmail.com")
