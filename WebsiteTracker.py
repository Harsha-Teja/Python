import smtplib
import requests

# Enter your website url here. You can more than one as its a list
check = ["https://teacherr.in"]

# Write your email-id and password. Better if you could alos use the os.environ variable which is more secure
EMAIL_ADDRESS = "************@gmail.com"
EMAIL_PASSWORD = "*************"

# Setting up the traffic
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Write the subject and content to be displayed in the main body
    subject = f"Check your website: {check} ==>This page is not working"
    Body = """There's some error in this page :{check}


Regards,
Harsha
    """

    msg = f"Subject: {subject}\n\n{Body}"

# This snippet is to check the status code of the website. Code 200 indicates good (working site).
for url in check:
    response = requests.get(url)
    status = response.status_code
    print(status)
    if status != 200:
        # Asking if the url status doesn't response with code 200 then mail the url to the receiver mentioned
        smtp.sendmail(
            EMAIL_ADDRESS,
            # The receiver email adress
            "**************@gmail.com",
            msg,
        )
