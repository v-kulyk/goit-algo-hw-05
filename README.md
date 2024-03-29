## Результати вимірювання ефективності алгоритмів до завдання №3

### Час виконання для існуючого підрядка:

(Text 1) Boyer-Moore: 0.00019205100034014322

(Text 2) Boyer-Moore: 0.0002546969990362413

(Text 1) KMP: 0.00206259300102829

(Text 2) KMP: 0.0019026269983442035

(Text 1) Rabin-Karp: 0.004479835002712207

(Text 2) Rabin-Karp: 0.004323647997807711

Час виконання для не існуючого підрядка:

(Text 1) Boyer-Moore: 0.0004011589990113862

(Text 2) Boyer-Moore: 0.0005794130011054222

(Text 1) KMP: 0.0019055670018133242

(Text 2) KMP: 0.0030386189973796718

(Text 1) Rabin-Karp: 0.005996142997901188

(Text 2) Rabin-Karp: 0.008053326997469412

### Висновок

Базуючись на отриманих результатах, зробимо висновки щодо швидкостей 
алгоритмів для кожного тексту окремо та в цілому:

### Для існуючого підрядка:

Text 1:

Найшвидшим алгоритмом для Text 1 є Boyer-Moore (0.000192 сек).

Text 2:

Найшвидшим алгоритмом для Text 2 також є Boyer-Moore (0.000255 сек).

### Для неіснуючого підрядка:

Text 1:

Найшвидшим алгоритмом для Text 1 є Boyer-Moore (0.000401 сек).

Text 2:

Найшвидшим алгоритмом для Text 2 також є Boyer-Moore (0.000579 сек).

### Загальні Висновки:

Порівнюючи алгоритми в цілому для обох текстів,
Boyer-Moore показав найкращі результати як для існуючого, так і для неіснуючого підрядка для обох текстів.
KMP та Rabin-Karp також доволі ефективні.
