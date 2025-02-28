import time
import re
import hyperloglog

def load_ip_addresses(log_file):
    """
    Завантажує IP-адреси з лог-файлу, ігноруючи некоректні рядки.
    """
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ip_addresses = []
    
    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = ip_pattern.search(line)
            if match:
                ip_addresses.append(match.group())
    
    return ip_addresses

def count_unique_ips_set(ip_addresses):
    """
    Точний підрахунок унікальних IP-адрес за допомогою set.
    """
    return len(set(ip_addresses))

def count_unique_ips_hyperloglog(ip_addresses):
    """
    Наближений підрахунок унікальних IP-адрес за допомогою HyperLogLog.
    """
    hll = hyperloglog.HyperLogLog(0.01)  # Параметр 0.01 - визначає точність
    for ip in ip_addresses:
        hll.add(ip)
    return len(hll)

if __name__ == "__main__":
    log_file = "lms-stage-access.log"  # Замініть на актуальний шлях до файлу
    
    # Завантаження IP-адрес
    ip_addresses = load_ip_addresses(log_file)
    print(f"Завантажено {len(ip_addresses)} IP-адрес")
    
    # Точний підрахунок
    start_time = time.time()
    exact_count = count_unique_ips_set(ip_addresses)
    exact_time = time.time() - start_time
    
    # HyperLogLog підрахунок
    start_time = time.time()
    hll_count = count_unique_ips_hyperloglog(ip_addresses)
    hll_time = time.time() - start_time
    
    # Вивід результатів
    print("Результати порівняння:")
    print(f"{'Метод':<25} {'Унікальні елементи':<20} {'Час виконання (сек.)':<20}")
    print(f"{'Точний підрахунок':<25} {exact_count:<20} {exact_time:<20.5f}")
    print(f"{'HyperLogLog':<25} {hll_count:<20} {hll_time:<20.5f}")
