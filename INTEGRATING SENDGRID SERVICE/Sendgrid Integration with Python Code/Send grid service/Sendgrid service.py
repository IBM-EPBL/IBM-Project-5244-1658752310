import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import mail

export SENDGRID_API_KEY=<SG.W1UvV2NTSPa58clsfTq5yg.iEzLjyk_5Yv_DI1sffihutJo8ytg4ikx6GKDHYgyKDH2QmhnEM>

message = Mail(
    from_email = "somu93739@gmail.com";
    to_email = "vh10119_ece19@velhightech.com"
    subject="test";
    html_content = "<p>hi</hi>"
)

try:
    sg = SendGridAPIClient({SENDGRID_API_KEY})
    response = sg.send(message)
except EXCEPTION as e:
    print(e)