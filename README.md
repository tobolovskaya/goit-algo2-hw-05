# Алгоритми роботи з великими даними

## Опис проекту
Цей проект містить дві основні задачі:
1. **Перевірка унікальності паролів за допомогою фільтра Блума**.
2. **Порівняння продуктивності HyperLogLog із точним підрахунком унікальних елементів**.

Проект демонструє ефективні методи роботи з великими наборами даних, використовуючи наближені структури даних для оптимізації пам'яті та швидкості обробки.

---
## Завдання 1: Перевірка унікальності паролів за допомогою фільтра Блума

### Опис
Реалізується **фільтр Блума**, який дозволяє визначати, чи використовувався пароль раніше, без збереження самих паролів. Це значно зменшує використання пам’яті при роботі з великими обсягами даних.

### Технічні умови
- **Клас `BloomFilter`** реалізує додавання елементів у фільтр та перевірку наявності елемента.
- **Функція `check_password_uniqueness`** перевіряє нові паролі на унікальність.
- Обробка помилкових даних та підтримка масштабованості.

### Запуск коду
```python
if __name__ == "__main__":
    bloom = BloomFilter(size=1000, num_hashes=3)
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)
    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")
```

### Очікуваний результат
```
Пароль 'password123' — вже використаний.
Пароль 'newpassword' — унікальний.
Пароль 'admin123' — вже використаний.
Пароль 'guest' — унікальний.
```

---
## Завдання 2: Порівняння продуктивності HyperLogLog із точним підрахунком унікальних елементів

### Опис
У цьому завданні порівнюються два методи підрахунку унікальних IP-адрес з лог-файлу:
1. **Точний підрахунок** за допомогою `set()`.
2. **Наближений підрахунок** за допомогою `HyperLogLog`.

### Технічні умови
- Завантаження лог-файлу `lms-stage-access.log` та обробка IP-адрес.
- Реалізація точного підрахунку унікальних IP-адрес.
- Реалізація підрахунку через `HyperLogLog`.
- Порівняння за точністю та часом виконання.

### Запуск коду
```python
if __name__ == "__main__":
    log_file = "lms-stage-access.log"
    ip_addresses = load_ip_addresses(log_file)
    start_time = time.time()
    exact_count = count_unique_ips_set(ip_addresses)
    exact_time = time.time() - start_time
    start_time = time.time()
    hll_count = count_unique_ips_hyperloglog(ip_addresses)
    hll_time = time.time() - start_time
    print("Результати порівняння:")
    print(f"{'Метод':<25} {'Унікальні елементи':<20} {'Час виконання (сек.)':<20}")
    print(f"{'Точний підрахунок':<25} {exact_count:<20} {exact_time:<20.5f}")
    print(f"{'HyperLogLog':<25} {hll_count:<20} {hll_time:<20.5f}")
```

### Очікуваний результат
```
Результати порівняння:
Метод                     Унікальні елементи    Час виконання (сек.)    
Точний підрахунок         80000                 0.72                    
HyperLogLog               79645                 0.08                    
```

---
## Висновки
- **Фільтр Блума** ефективно працює з перевіркою унікальності паролів без необхідності їхнього збереження.
- **HyperLogLog** дозволяє швидко оцінити кількість унікальних IP-адрес з незначною похибкою, значно перевершуючи `set()` за продуктивністю.

Цей проект демонструє сучасні підходи до роботи з великими даними та оптимізації підрахунку унікальних елементів. 🚀

