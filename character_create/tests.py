from django.test import TestCase
from django.contrib.auth.models import User
from .models import Character

class CharacterTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='abc123')
        testuser1.save()

        test_character_create = Character.objects.create(
            author=testuser1,
            name='Test Character',
            species='Human',
            char_class='Warrior',
            level=1,
            created_on='2022-12-20 14:47:00.000000+00:00',)
        test_character_create.save()

    def test_character_data(self):
        character = Character.objects.get(id=1)
        author = f'{character.author}'
        name = f'{character.name}'
        species = f'{character.species}'
        char_class = f'{character.char_class}'
        level = f'{character.level}'
        created_on = f'{character.created_on}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(name, 'Test Character')
        self.assertEqual(species, 'Human')
        self.assertEqual(char_class, 'Warrior')
        self.assertEqual(level, '1')
        self.assertEqual(created_on, '2022-12-20 14:47:00+00:00')

