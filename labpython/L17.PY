car1 = {
"Maruti ": "1981 ",
"model": "alto "

}
print("car1 : ", car1)
car2 = {
"Hyundai": "1996",
"model": "Nexo"

}
print("car2 : ", car2)
print("")
car = car1.copy()
car.update(car2)

print("after merging : ", car)
