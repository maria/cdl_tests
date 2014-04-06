import factory


class UserFactory(factory.DjangoModelFactory):

    FACTORY_FOR = 'User'

    firstname = factory.Sequence(lambda n: "Firstname-%s" % str(n))
    lasttname = factory.Sequence(lambda n: "Lastname-%s" % str(n))
    password = "password"
