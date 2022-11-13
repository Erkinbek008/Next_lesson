# Birinchi kod to`g`ri
# Ikkinchisida else xato , siz elsedagi qiymat yani splitni boshida qilishingiz kerak edi!
# Chunki unga agarda raqam yoki xech narsa kiritmasak bizga NameErrorni keltirib chiqaradi!
# Keyin oxiridagi printni ichiga kirgizibsiz lekin unday bo`lmaydi. Siz oxiridagi printni ichiga solmang!
# Siz albatta yutasiz!!!
# 1 - masala
text = input("Matn kiriting: ")
sozlar = text.split()
print(len(sozlar))


# 2 - masala
text = input("Matn kiriting: ")
sozlar = text.split()
if text.isdigit():
    print("Siz raqam kiritdingiz menga matn kiriting  ")
elif text == "":
    print ("Siz hech narsa kiritmadingiz  ")
print(f"Matnda {len(sozlar)} so'z mavjud  ")