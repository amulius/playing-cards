import factory
from ..models import Player


class WarGameFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'cards.WarGame'


class PlayerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Player
    username = factory.Sequence(lambda i: 'User{}'.format(i))
    password = factory.PostGenerationMethodCall('set_password',
                                                'password')
    email = 'test@test.com'
    phone = '555-555-5555'
