# 0/1 Knapsack Problem - Dynamic Programming
# Kasus: Tim Ekspedisi Pendakian Gunung

items = [
    ("Tenda Ringan", 5, 30),
    ("Kompor Portable", 3, 20),
    ("Sleeping Bag", 4, 25),
    ("Matras", 2, 12),
    ("Jaket Gunung", 2, 14),
    ("Peralatan Masak", 4, 22),
    ("Lampu Headlamp", 1, 8),
    ("Botol Air Cadangan", 3, 18),
    ("P3K", 1, 10),
    ("GPS Tracker", 2, 16)
]

capacity = 15
n = len(items)

# Membuat tabel DP
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Mengisi tabel DP
for i in range(1, n + 1):
    weight = items[i - 1][1]
    value = items[i - 1][2]
    for w in range(capacity + 1):
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w],
                           dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

# Menentukan item yang terpilih
w = capacity
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(items[i - 1][0])
        w -= items[i - 1][1]

selected_items.reverse()

# Output hasil
print("Nilai maksimum:", dp[n][capacity])
print("Item terpilih:")
for item in selected_items:
    print("-", item)

total_weight = sum(item[1] for item in items if item[0] in selected_items)
print("Total berat:", total_weight, "kg")
