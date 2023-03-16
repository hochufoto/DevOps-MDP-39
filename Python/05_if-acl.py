# Объявляем переменную aclNum
aclNum = int(input("What is the IPv4 ACL number? "))
# Проверяем на соответствие от 1 до 99
if aclNum >= 1 and aclNum <= 99:
# Выводим результат
    print("This is a standard IPv4 ACL. ")
# Проверяем на соответствие от 100 до 199    
elif aclNum >= 100 and aclNum <= 199:
# Выводим результат
    print("This is a extended IPv4 ACL. ")
# Если оба варианта не подошли идем сюда!
else:
# Выводим результат
    print("This is not a standart or extended IPv4 ACL. ")