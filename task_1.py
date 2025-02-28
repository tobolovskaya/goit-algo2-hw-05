import mmh3
import bitarray

class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        """
        Ініціалізує фільтр Блума.
        :param size: Розмір бітового масиву
        :param num_hashes: Кількість хеш-функцій
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)
    
    def _hashes(self, item: str):
        """
        Генерує кілька хешів для заданого елемента.
        """
        return [mmh3.hash(item, i) % self.size for i in range(self.num_hashes)]
    
    def add(self, item: str):
        """
        Додає елемент до фільтра Блума.
        """
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1
    
    def contains(self, item: str) -> bool:
        """
        Перевіряє, чи міститься елемент у фільтрі Блума.
        """
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))

def check_password_uniqueness(bloom: BloomFilter, passwords: list) -> dict:
    """
    Перевіряє унікальність паролів за допомогою фільтра Блума.
    :param bloom: Об'єкт BloomFilter
    :param passwords: Список паролів для перевірки
    :return: Словник результатів перевірки
    """
    results = {}
    for password in passwords:
        if not isinstance(password, str) or not password:
            results[password] = "Некоректне значення"
        elif bloom.contains(password):
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
            bloom.add(password)
    return results

if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)
    
    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)
    
    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)
    
    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")