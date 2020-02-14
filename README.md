# ContactApp
Built a Python Web App using Flask, PostgreSQL &amp; Heroku.

The Web App is accessible via http://steffen-feedback-app1.herokuapp.com

As soon as you submit your request, an email is sent to my personal email adress and my database gets updated!

# Quick Start
```
Don't forget to add your DATABASE URI in app.py and your mail params in send_mail.py
```

### Install dependencies
```
pipenv shell
pipenv install
```

### Serve on localhost:5000
```
python app.py
```


# Python Heroku Deployment

> Steps to create a postgres database and deply a Python app to Heroku

### Install guinicorn locally
```
pipenv install gunicorn
or
pip install gunicorn
```

### Install Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli

### Login via CLI
```
heroku login
```

### Create app
```
heroku create appname
```

### Create database
```
heroku addons:create heroku-postgresql:hobby-dev --app appname
```

### Get URI
```
heroku config --app appname

# Add to your app
```

### Create Procfile
```
touch Procfile

# Add this
web: gunicorn app:app
```

### Create requirements.txt
```
pip freeze > requirements.txt
```

### Create runtime.txt
```
touch runtime.txt

# Add this
python-3.7.2
```

### Deploy with Git
```
git init
git add . && git commit -m 'Deploy'
heroku git:remote -a appname
git push heroku master
```

### Add table to remote database
```
heroku run python
>>> from app import db
>>> db.create_all()
>>>exit()
```
### Visit app
```
heroku open
```
