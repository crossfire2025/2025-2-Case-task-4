def max_dragon_power(n):
    if n == 0:
        return 0

    max_power = 0

    for sevens in range(n // 7 + 1):
        remaining = n - sevens * 7

        for threes in range(remaining // 3 + 1):
            rest = remaining - threes * 3

            for twos in range(rest // 2 + 1):
                ones = rest - twos * 2

                total_heads = sevens * 7 + threes * 3 + twos * 2 + ones
                if total_heads == n:
                    power = (7 ** sevens) * (3 ** threes) * (2 ** twos) * (1 ** ones)
                    max_power = max(max_power, power)

    return max_power

def main():
    print("=== Расчёт силы драконьей стаи ===")
    print("Введите количество голов (от 1 до 99), или 'выход' для завершения.\n")

    while True:
        user_input = input("Введите количество голов: ").strip().lower()

        if user_input in ['выход', 'exit']:
            print("Завершение программы.")
            break

        if not user_input.isdigit():
            print("Ошибка: введите натуральное число от 1 до 99.")
            continue

        n = int(user_input)
        if not (0 < n < 100):
            print("Ошибка: число должно быть от 1 до 99.")
            continue

        power = max_dragon_power(n)
        print(f"Максимальная сила стаи при {n} головах: {power}\n")

if __name__ == "__main__":
    main()
