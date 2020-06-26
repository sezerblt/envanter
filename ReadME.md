
#Polls
Polls is a Django app to conduct Web-based polls. For each question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

#Quick start
Add "polls" to your INSTALLED_APPS setting like this:

INSTALLED_APPS = [
    ...
    'myapp',
    'users',
    'rest_framework',
]
Include the polls URLconf in your project urls.py like this:

path('polls/', include('myapp.urls')),
Run python manage.py migrate to create the app models.

Start the development server and visit http://127.0.0.1:8000/admin/ to create a poll (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/ to participate in the our app
#pip instaii djano
#pip install rest_framework
#pip install Pillow
#pip install capturex
#pip install crispy_form
