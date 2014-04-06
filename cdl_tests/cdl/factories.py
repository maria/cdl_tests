import factory

import models


class UserFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.User

    firstname = factory.Sequence(lambda n: "Firstname-%s" % str(n))
    lastname = factory.Sequence(lambda n: "Lastname-%s" % str(n))
    password = "password"
