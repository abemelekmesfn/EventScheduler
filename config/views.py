from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Event Scheduler API</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f7f7f7; }
                    h1 { color: #333; }
                    p { font-size: 18px; color: #555; }
                    code { background: #eee; padding: 2px 5px; border-radius: 3px; }
                </style>
            </head>
            <body>
                <h1>🚀 Welcome to the Event Scheduler API</h1>
                <p>This is a backend API built with Django REST Framework.</p>
                <p>Try accessing endpoints by typing them in the browser bar, for example:</p>
                <ul style="list-style:none; padding:0;">
                    <li><code>/api/users/</code> → List of users</li>
                    <li><code>/api/events/</code> → List of events</li>
                    <li><code>/api/participants/</code> → List of participants</li>
                    <li><code>/api/reminders/</code> → List of reminders</li>
                </ul>
                <p>Authentication is required for some endpoints.</p>
                <p><i>Test account:</i><br>
                   Username: <b>abemelek</b><br>
                   Email: <b>test@example.com</b><br>
                   Password: <b>password123</b></p>
            </body>
        </html>
    """)
