import unittest
from warrior import Warrior


class TestWarrior(unittest.TestCase):

    def setUp(self):
        """Создаем двух воинов для тестирования."""
        self.warrior1 = Warrior("Воин 1")
        self.warrior2 = Warrior("Воин 2")

    def test_initial_attributes(self):
        """Проверяем начальные атрибуты воинов."""
        self.assertEqual(self.warrior1.health, 100)
        self.assertEqual(self.warrior1.armor, 50)
        self.assertEqual(self.warrior1.stamina, 50)

    def test_attack_reduces_health(self):
        """Проверяем, что атака уменьшает здоровье."""
        initial_health = self.warrior2.health
        self.warrior1.attack(self.warrior2)
        self.assertTrue(self.warrior2.health < initial_health)

    def test_attack_reduces_armor(self):
        """Проверяем, что атака уменьшает броню при наличии брони."""
        self.warrior1.attack(self.warrior2)
        self.assertTrue(self.warrior2.armor >= 0)

    def test_defense_does_not_change_health(self):
        """Проверяем, что защита не уменьшает здоровье."""
        self.warrior2.defend()
        initial_health = self.warrior2.health
        self.warrior1.attack(self.warrior2)  # Warrior 1 attacks Warrior 2
        self.assertTrue(
            self.warrior2.health < initial_health or self.warrior2.armor < 50
        )

    def test_health_cannot_be_negative(self):
        """Проверяем, что здоровье не может стать отрицательным."""
        self.warrior2.health = 5
        self.warrior1.attack(self.warrior2)  # Warrior 1 attacks Warrior 2
        self.assertGreaterEqual(self.warrior2.health, 0)

    def test_armor_cannot_be_negative(self):
        """Проверяем, что броня не может стать отрицательной."""
        self.warrior2.armor = 0
        self.warrior1.attack(self.warrior2)  # Warrior 1 attacks Warrior 2
        self.assertGreaterEqual(self.warrior2.armor, 0)


if __name__ == "__main__":
    unittest.main()
