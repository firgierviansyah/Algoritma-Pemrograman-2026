print("PROGRAM MENENTUKAN SUKU KE-n BARISAN ARITMETIKA")
print()

# Memasukkan barisan aritmetika
barisan = input("Masukkan barisan aritmetika yang diketahui: ")

# Mengubah input menjadi daftar angka
suku = [float(x.strip()) for x in barisan.split(",")]

# Memastikan minimal ada dua suku
if len(suku) < 2:
    print("Barisan harus memiliki minimal dua suku.")
else:
    # Menentukan suku pertama dan beda
    suku_pertama = suku[0]
    beda = suku[1] - suku[0]

    # Menentukan suku yang ingin dicari
    n = int(input("Ingin mencari suku ke berapa? "))

    # Menghitung suku ke-n
    suku_ke_n = suku_pertama + (n - 1) * beda

    # Menampilkan hasil
    print()
    print("HASIL PERHITUNGAN")

    if suku_pertama.is_integer():
        print("Suku pertama :", int(suku_pertama))
    else:
        print("Suku pertama :", suku_pertama)

    if beda.is_integer():
        print("Beda         :", int(beda))
    else:
        print("Beda         :", beda)

    if suku_ke_n.is_integer():
        print("Suku ke-", n, "   :", int(suku_ke_n))
    else:
        print("Suku ke-", n, "   :", suku_ke_n)