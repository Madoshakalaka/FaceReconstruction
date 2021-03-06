# How to Use

Make sure you're using python 3

On command line:

    cd to FaceReconstruction-master

    pip install -r requirements.txt

    python manage.py runserver

The above runs the server on http://127.0.0.1:8000/, paste it to the browser to view the website.

To submit/download files and do face reconstruction on arbitrary faces, an extra tcp server needs to be run, the 
steps are (before you upload files on the web-page):

    clone https://github.com/YadiraF/PRNet
    move serverScript.py to the directory of the cloned library
    cd to the cloned libarary
    use python2.7
    pip install -r requirements
    run serverScript.py

## (For collaborators) To Edit Web-page in Django Framework
html is located at: ` \index.html`

css is located at: `FaceReconstruction-master\modelEval\static\modelEval\css`

js is located at: `FaceReconstruction-master\modelEval\static\modelEval\js`

There are sometimes `{% ... %}` or `{{...}}` in the html
For example:

    {% static 'modelEval/js/jqeury.js' %}
    {%if result%}yes{% else %}no{% endif %}
    {{greetings}}

These are called **tags**. It's a DJANGO feature for dynamic web page. Django will parse the html first to remove tags and generate proper html, and display the parsed html as a response.


back-end code to deal with url requests mainly resides in  `FaceReconstruction-master\FaceReconstruction-master\modelEval\views`

    def index(request):
        ...

This is the function that handles url requests.

## more

to learn how template parsing works:
https://www.tutorialspoint.com/django/django_template_system.htm


