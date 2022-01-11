# Rupa Email Client


### Prerequisites
**Docker** OR **Python 3**

## Setup


### Env
- Add API Keys from Sendgrid and Mailgun to .env respectively
- Add Mailgun domain name to .env
- Modify which email service to use by updating `EMAIL_CLIENT` to `mailgun` or `sendgrid`

### Docker
```
$ docker build --tag rupa .
$ docker run -d -p 5000:5000 rupa
```

### Virtualenv
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python3 -m flask run
```


## Run Tests
```
$ python -m unittest
```

### Docker
# 

## Technology choices & Dependency decisions
- **python3** -- Easy to read and minimal effort for simple web servers.
- **Docker** -- Standard for shipping applications in the most portable fashion
- **Flask** -- Very lightweight framework for webserver.  While this does add a dependency instead of simply leveraging the standard http library, it's .  Not necessary to pull in substantial packages like Django unless leveraging ORM or other built in features.
- **python-dotenv** -- Easy loading variables into environment automatically 
- **requests** -- Commonly recommended for http request use.  Package build on python http.client library.

## Additional work
- More unit tests on failure cases and edge cases
- More robust error handling of API calls
- Detailed error responses of bad parameters
- Investigate and refactor to leverage [asyncio package](https://flask.palletsprojects.com/en/2.0.x/async-await/)
- Add documentation for API utilization