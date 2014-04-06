# CDL Free for all

## Testing 

 - [Presentation](https://docs.google.com/presentation/d/1OPQ5B1FqVqzh7gzJ5rsj1mwCM3M1wvt8G46SAMQOs0g/edit?usp=sharing)
 - Demo:

    - test case
    - model
    - factory
    - Django app

### Demo

#### TestCase

  - Packages: `unittest`, `unittest2`
  - Runner: `nose`
  - Command: `nosetests test_user.py`


```python

class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        pass
```

Run the test, see it passes, `nosetests test_user.py`

#### Model

   - Describe a `User` model:

```python

class User(object):
    """Create a object with the expected attributes.
    We will transform it in a Django model later.
    """

    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

```

Import the class in the console, create an object of type `User`.

#### Factory

   - Package: `factory-boy`
   - Describe a factory for the `User` model:

```python
import factory


class UserFactory(factory.Factory):
    # Generate random strings for Users names, like: Name-1
    firstname = factory.Sequence(lambda n: "FirstName-%s" % str(n))
    lastname = factory.Sequence(lambda n: "LastName-%s" % str(n))

    # Create the same password for all users
    password = "Password"
```

#### Create Django project and app

  - Check if you have Django, otherwise install Django

```
  $ pip freeze | grep Django
  $ sudo pip install Django
```

  - Create Django project and app

```
$ django-admin.py startproject cdl_tests
$ cd cdl/
$ django-admin.py startapp cdl
```
  - Add `User` as a Django model:
      - `$ cd cdl_tests/cdl/`
      - open and edit `models.py`

```python
from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

```

As you can see we don't have a `__init__` method, we just define the model
attributes as class attributes.

  - Copy the factory class in a new factories file:

```
$ touch ~/cdl_tests/cdl/factories.py
```
and copy the class inside the file, [example](https://github.com/marianitadn/cdl_tests/blob/master/cdl_tests/cdl/factories.py).

    
  - Create the application Database and sync the models

```
  $ cd cdl_tests
  $ vim cdl_tests/settings.py
```
  
  - Update the project database configuration and installed apps lists, [example](https://github.com/marianitadn/cdl_tests/commit/83389abdb55cc644b98edc8c8fffd0d855cec9df)
  - Sync the database: `$ python manage.py syncdb`


#### Copy and run the tests

  - Copy the test case inside the project in the file `~/cdl_tests/cdl/tests.py`, [example](https://github.com/marianitadn/cdl_tests/blob/master/cdl_tests/cdl/tests.py)

  - Run all the project tests, with the command: `python manage.py test`
  
The runner is build in Django, no need to use `nosetests` anymore.


####

If you have any questions open an issue.

Thanks! :)

