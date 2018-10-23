# Building a web-app with Flask

- Create an instance of the `Flask` class
  - This helps Flask figure out where app dependencies exist
- `app.run()` starts a development server
- Minimum boilerplate required

```
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
```

- Flask provides many `decorators`
  - `app.route()` is the most widely used

- Web apps are dynamic, they generate HTML on the fly
  - Static HTML inside Flask code would become messy
  - We write HTML code as **templates**
  - These are filled based on the logic of the app
  - Flask uses the Jinja2 templating language for creating and filling placeholders

- Users can interact with the app through `forms`
    - `GET` or `POST` requests can be initiated using elements like `form` and `input`

- `request`
  - provides data submitted via GET or POST requests on a page
  - we use the `name` attribute of the particular HTML form element
  - In `shopping.py`, we fetch the data submitted via a form element with name='item' with `request.form['item'`

- `redirect` and `url_for`
  - used for loading specific pages after a user completes an action
  - for example; redirecting users to their profile page upon successful login
  - `url_for` takes the name of the function that produces the target page

- `jsonify`
  - converts Python objects to JSON
  - useful when building APIs that provide data to programs
