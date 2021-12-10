spisok=[]
numbers=[1,2,3,4,5]
abc=["Abc","B","С"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
	print("1-добавить букву в список")
	print("2-склеить списки")
	print("3-Добавление буквы в опеределённое место")
	print("4-удалить букву")
	print("5- написать слово заглавными буквами")
	print("6- написать слово маленькими буквами")
	print("7- проверить состоит ли вся строка из заглавных букв")
	valik=int(input())
	if valik==1:
		a=input("Введи букву")
		slovo_list.append(a)
		print(f"Добавили {a} новый список", slovo_list)
	elif valik==2:
		slovo_list.extend(abc)
		print()
	elif valik==3:
		a=input("Введи букву которую хочешь добавить")
		i=int(input("Введи номер позиции, куда хочешь добавить букву"))
	elif valik==4:
		a=input("Введи букву которую хочешь удалить.")
		slovo_list.remove(a)
		print(slovo_list)
	elif valik==5:
		print(slovo.upper()) #пишит все буквы заглвными
	elif valik==6:
		print(slovo.lower()) #пишит все буквы маленькими
	elif valik==7:
		print(slovo.isupper()) #проверяет изначальное слово, состоит ли оно из заглавных букв