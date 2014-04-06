# CDL Free for all

## Testing 

 - [Prezentare]()
 - Demo:

    - test case
    - model
    - factory
    - Django app

### Demo

#### TestCase
  - Pachete: `unittest`, `unittest2`
  - Runner: `nose`
  - Command: `nosetests test_use.py`


```python

class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        pass
```

Run the test, see it passes.

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
   - Describe a factory for the `User` model, `UserFactory`:

```python
import factory


class UserFactory(factory.Factory):
    FACTORY_FOR = 'User'

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
        - ` $ cd `cdl_tests/cdl/`
        - open `models.py`

```python
from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

```

As you can see we don't have a `__init__` method, we just define the model
attributes as class attributes.

    - Copy the factory class:

```
$ mkdir cdl_tests/cdl/tests/factories
$ cp user_factory.py ~/cdl_tests/cdl/tests/factories/.`
```
    
    - Create the application Database and sync the models

```
$ cd cdl_tests
$ vim cdl_tests/settings.py
```
    - Update the file database and installed apps lists - check the file in the
repo.

    - Sync the database

```$ python manage.py syncdb```


#### Copy and run the tests

 - ```cp test_user.py cdl_tests/cdl/tests/.```

 - ```python manage.py test cdl/tests/test_user.py```

