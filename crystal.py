import os
value = os.getenv("CRYSTAL","")
print(f'My nickname is {value}')

favorite_snack = os.getenv("SNACK","")
print(f'My favorite snack is {favorite_snack}')
