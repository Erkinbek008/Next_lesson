# 1 .Siz isdigitni isdiget deb yozgansiz
# Men bu kodga Bo`sh katak ni ham kiritdim
# Siz albatta yutasiz
nimadur = input("Biror narsa kiriting:  ")
if nimadur.isdigit():
    print("Bu raqam ")
elif len(nimadur) ==0 or nimadur == "":
    print("Hech narsa kiritilmadi ")
elif len(nimadur)==1:
    print("Bu harf ")
elif nimadur == " ":
    print("Bo`sh katak")
else:
    print("Bu matn ")