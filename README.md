# Using CockroachDB with a Python + Flask App

Build a full-stack web app that simulates a game leaderboard using the simplicity of Python with a Flask web development framework. The corresponding blog post is available via [https://www.cockroachlabs.com/blog/sample-app-python-and-cockroachdb/](https://www.cockroachlabs.com/blog/sample-app-python-and-cockroachdb/).

The Flask web framework works in the application’s backend. It relies on Jinja2 as a rich templating engine for the frontend to render HTML when users request web pages. This application connects to CockroachDB via Serverless using SQLAlchemy, an open source object-relational mapper for the Python language. Finally, we use Heroku to deploy the sample app, where everything works exactly the same as on the local system.

To run the app, clone or fork the code into your own GitHub repo, use the repo to create a new Heroku app, set the DB_URI variable in Heroku to a Postgres connection string, and then deploy.
