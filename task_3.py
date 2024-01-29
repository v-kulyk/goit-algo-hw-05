import timeit


# Функція для пошуку підрядка за допомогою Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# Функція для пошуку підрядка за допомогою Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


# Функція для пошуку підрядка за допомогою Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


# Функція для вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


# Читаємо тексти з файлів
with open('text1.txt', 'r') as file:
    text1 = file.read()

with open('text2.txt', 'r') as file:
    text2 = file.read()

# Приклади підрядків для пошуку
# existing_pattern_text_1 = "обрати чергові найбільші за номіналом"
existing_pattern_text_1 = "обрати чергові найбільші "
# existing_pattern_text_2 = "булевих функцій у формі БДР стало можливим"
existing_pattern_text_2 = "булевих функцій у формі "
non_existing_pattern = "not_valid_pattern"


# Вимірюємо час для кожного алгоритму та кожного тексту
time_bm_text1 = measure_time(boyer_moore_search, text1, existing_pattern_text_1)
time_kmp_text1 = measure_time(kmp_search, text1, existing_pattern_text_1)
time_rk_text1 = measure_time(rabin_karp_search, text1, existing_pattern_text_1)
time_bm_text2 = measure_time(boyer_moore_search, text2, existing_pattern_text_2)
time_kmp_text2 = measure_time(kmp_search, text2, existing_pattern_text_2)
time_rk_text2 = measure_time(rabin_karp_search, text2, existing_pattern_text_2)


time_bm_text1_non_existing = measure_time(boyer_moore_search, text1, non_existing_pattern)
time_kmp_text1_non_existing = measure_time(kmp_search, text1, non_existing_pattern)
time_rk_text1_non_existing = measure_time(rabin_karp_search, text1, non_existing_pattern)
time_bm_text2_non_existing = measure_time(boyer_moore_search, text2, non_existing_pattern)
time_kmp_text2_non_existing = measure_time(kmp_search, text2, non_existing_pattern)
time_rk_text2_non_existing = measure_time(rabin_karp_search, text2, non_existing_pattern)

print("Час виконання для існуючого підрядка:")
print("(Text 1)Boyer-Moore:", time_bm_text1)
print("(Text 2)Boyer-Moore:", time_bm_text2)
print("(Text 1)KMP:", time_kmp_text1)
print("(Text 2)KMP:", time_kmp_text2)
print("(Text 1)Rabin-Karp:", time_rk_text1)
print("(Text 2)Rabin-Karp:", time_rk_text2)

print("Час виконання для не існуючого підрядка:")
print("(Text 1)Boyer-Moore:", time_bm_text1_non_existing)
print("(Text 2)Boyer-Moore:", time_bm_text2_non_existing)
print("(Text 1)KMP:", time_kmp_text1_non_existing)
print("(Text 2)KMP:", time_kmp_text2_non_existing)
print("(Text 1)Rabin-Karp:", time_rk_text1_non_existing)
print("(Text 2)Rabin-Karp:", time_rk_text2_non_existing)
