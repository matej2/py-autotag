# py-autotag

> When I was tagging images with AI hashtag generators I got a lot of incorrect or even inappropriate results. I was thinking I could somehow determine topic of hashtags withouth too much depending on AI (and its mistakes)

This application provides random hashtags based on keywords that you provide. Randomness of hashtags helps prevent shadowblocking (altrought I dont assure it).

You determine topics for your account. Those topics are search keywords that are used in this application. You can also define how much of each hashtags are going to be added.

Application gets its data from Instagram public API.

## Instructions

1. Make sure that `pipenv` is installed: `sudo -H pip install -U pipenv` ([source](https://stackoverflow.com/a/47898336))
2. Make virtual environment: `pipenv shell`
3. Install dependencies: `pipenv install
4. Run applcation: `python3 manage.py runserver` or `py manage.py runserver`
5. Create superuser: `py manage.py createsuperuser`, login and create another user in database

## Endpoints

- GET: `api/login`

Obtain authentication token.
Request body:

```
{
  'username': <name>,
  'password': <pass>
}
```

- GET: `localhost/tags/random`

Headers: `Authentication: Token <token>`
Request body:

`name`: Name of the keyword search
`count`: Number of random hashtags included in response

Example:
```
[
  {
    'name': 'handmade'
    'count': 5
  }
]
```
