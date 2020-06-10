# py-autotag

This application provides random hashtags based on keywords that you provide. Randomness of hashtags helps prevent shadowblocking (altrought I dont assure it).

Application gets its data from Instagram public API.

## Instructions

1. Make sure that `pipenv` is installed: `sudo -H pip install -U pipenv` ([source](https://stackoverflow.com/a/47898336))
2. Make virtual environment: `pipenv shell`
3. Install dependencies: `pipenv install`
4. Run applcation: `python3 manage.py runserver` or `py manage.py runserver`

## Endpoints

- GET: `api/login`

Obtain authentication token.

- GET: `localhost/tags/random`

Headers: `Authentication: Token <token>`

Request body:

```
[
  {
    'name': 'handmade'
    'count': 5
  }
]
```
