                                                # Exercise 1 a)
# def cel_mai_lung_subsir(string):
#     word_lst = str(string).split(" ")
#     longest_unique_word_fn = ""
#     for word in word_lst:
#         if len(set(word)) > len(set(longest_unique_word_fn)):
#             longest_unique_word_fn = word
#     return longest_unique_word_fn
#
#
# if __name__ == '__main__':
#     string = input("Enter a string of characters: ")
#     longest_unique_word = cel_mai_lung_subsir(string=string)
#     print(f"The longest word(repetitive character not counted) is: {longest_unique_word}")

                                                # Exercise 1 b)
# source: https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
# from itertools import permutations
#
#
# def genereaza_permutatii(lst):
#     all_permutations = permutations(lst)
#     for permutation in all_permutations:
#         print(permutation)
#
#
# if __name__ == '__main__':
#     my_list = []
#     while True:
#         elem = input("Enter a word to add to your list(x to finish adding and show permutations): ")
#         if elem != "x" and elem != "X":
#             my_list.append(elem)
#         else:
#             genereaza_permutatii(lst=my_list)
#             break

                                                # Exercise 2 a)
# class MagazinOnline:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, name, type, price):
#         product = Product(name, type, price)
#         self.products.append(product)
#
#     def update_product(self, index, name, type, price):
#         self.products[index - 1].update(name, type, price)
#         print("Product updated successfully!")
#
#     def delete_product(self, index):
#         del self.products[index - 1]
#         print("Product deleted successfully!")
#
#     def find_product(self, index):
#         print(f"\nFound product with id = [{index}]:")
#         print(self.products[index-1])
#
#     def show_all_products(self):
#         for index, prod in enumerate(self.products):
#             print(f"{index+1}. {prod}\n")
#
#     def product_length(self):
#         return len(self.products)
#
#
# class Product:
#     def __init__(self, name, type, price):
#         self.name = name
#         self.type= type
#         self.price = price
#
#     def update(self, name, type, price):
#         if name:
#             self.name = name
#         if type:
#             self.type = type
#         if price:
#             self.price = price
#
#     def __str__(self):
#         return f"Name: {self.name}\nType: {self.type}\nPrice: {self.price:.2f}$"
#
#
# def verify_price(price):
#     while True:
#         try:
#             verified_price = float(price)
#             return verified_price
#         except ValueError:
#             print("Enter a valid numeric value for price!")
#             price = input("Enter the price of the product($): ")
#         except Exception:
#             print("Something went wrong!")
#             price = input("Enter the price of the product($): ")
#
#
# def verify_id(id):
#     while True:
#         try:
#             verified_id = int(id)
#             return verified_id
#         except TypeError:
#             print("Enter the correct id of the product!")
#             id = input("Enter the id of the product you want to modify: ")
#         except Exception:
#             print("Something went wrong!")
#             id = input("Enter the id of the product you want to modify: ")
#
#
# def update_menu():
#     products.show_all_products()
#     if products.product_length():
#         id = verify_id(input("Enter the id of the product you want to modify: "))
#         if id < 1 or id > products.product_length():
#             print("Invalid id entered!")
#             return
#     else:
#         print("There aren't any created products yet!")
#         return
#     name = ""
#     type = ""
#     price = 0
#
#     print()
#     while True:
#         print("1. Modify product name")
#         print("2. Modify product type")
#         print("3. Modify product price")
#         print("X. Stop modifying product")
#         option = input("\nEnter your option: ")
#         match option:
#             case "1":
#                 name = input("Enter the new name of your product: ")
#             case "2":
#                 type = input("Enter the new type of your product: ")
#             case "3":
#                 price = verify_price(input("Enter the price of your product($): "))
#             case "x":
#                 products.update_product(id, name, type, price)
#                 break
#             case "X":
#                 products.update_product(id, name, type, price)
#                 break
#             case _:
#                 print("Invalid option!")
#
#
# def clear_screen():
#     time.sleep(0.5)
#     print("\n")
#
#
# def menu():
#     global products
#     print("Welcome to my Online Shop App!")
#     while True:
#         print("1. Add a new product")
#         print("2. Update current products")
#         print("3. Delete current products")
#         print("4. Search product")
#         print("5. See all current products")
#         print("X. Exit App")
#         choice = input("\nEnter your choice: ")
#         print()
#
#         match choice:
#             case "1":
#                 name = input("Enter the name of your product: ")
#                 type = input("Enter the type of your product: ")
#                 price = verify_price(input("Enter the price of your product($): "))
#                 products.add_product(name, type, price)
#                 clear_screen()
#             case "2":
#                 update_menu()
#                 clear_screen()
#             case "3":
#                 products.show_all_products()
#                 if products.product_length():
#                     id = verify_id(input("Enter the id of the product you want to delete: "))
#                     if id < 1 or id > products.product_length():
#                         print("Invalid id entered!")
#                     else:
#                         products.delete_product(id)
#                 else:
#                     print("There aren't any created products yet!")
#                 clear_screen()
#             case "4":
#                 if products.product_length():
#                     id = verify_id(input("Enter the id of the product you want to find: "))
#                     if id < 1 or id > products.product_length():
#                         print("Invalid id entered!")
#                     else:
#                         products.find_product(id)
#                 else:
#                     print("There aren't any created products yet!")
#                 clear_screen()
#             case "5":
#                 products.show_all_products()
#                 time.sleep(1)
#                 print()
#             case "x":
#                 break
#             case "X":
#                 break
#             case _:
#                 print("Invalid choice!")
#                 clear_screen()
#
#
# if __name__ == '__main__':
#     products = MagazinOnline()
#     menu()

                                                    # Exercise 2 b)
# import random
#
# class JocVideo:
#     def __init__(self):
#         self.dinosaurs = [
#             TRex(),
#             Triceratops(),
#             Spinosaurus(),
#             Velociraptor(),
#             Stegosaurus(),
#             Brachiosaurus(),
#             Diplodoc()
#     ]
#
#     def get_random_dino(self):
#         random_index = random.randint(0, 6)
#         return self.dinosaurs[random_index]
#
#     def get_specific_dino(self, index):
#         return self.dinosaurs[index-1]
#
#
#     def fight(self, dino1, dino2):
#         print(f"{dino1.name} is attacking {dino2.name}!")
#
#         dino1_initial_hp = dino1.hp
#         dino2_initial_hp = dino2.hp
#
#         dino1_attack_time = 1/dino1.attack_speed
#         dino2_attack_time = 1/dino2.attack_speed
#
#         while dino1.hp > 0 and dino2.hp > 0:
#             while dino1_attack_time <= dino2_attack_time:
#                 time.sleep(1/dino1.attack_speed)
#                 if dino2.hp - dino1.damage >= 0:
#                     print(f"{dino1.name} attacks {dino2.name} for {dino1.damage:.2f} damage! {dino2.name} "
#                           f"HP left: {dino2.hp-dino1.damage:.2f}")
#                 else:
#                     print(f"{dino1.name} attacks {dino2.name} for {dino1.damage:.2f} damage! {dino2.name} "
#                           f"HP left: 0.00")
#                 dino2.hp -= dino1.damage
#                 dino1_attack_time += 1/dino1.attack_speed
#
#                 if dino2.hp <= 0:
#                     print(f"[{dino2.name} has been defeated! +45 coins for {dino1.name}! Use them wisely!]\n")
#                     dino1.money += 45
#                     dino1.hp = dino1_initial_hp
#                     dino2.hp = dino2_initial_hp
#                     return
#
#             while dino2_attack_time <= dino1_attack_time:
#                 time.sleep(1/dino2.attack_speed)
#                 if dino1.hp - dino2.damage >= 0:
#                     print(f"{dino2.name} attacks {dino1.name} for {dino2.damage:.2f} damage! {dino1.name} "
#                           f"HP left: {dino1.hp-dino2.damage:.2f}")
#                 else:
#                     print(f"{dino2.name} attacks {dino1.name} for {dino2.damage:.2f} damage! {dino1.name} "
#                           f"HP left: 0.00")
#                 dino1.hp -= dino2.damage
#                 dino2_attack_time += 1/dino2.attack_speed
#
#                 if dino1.hp <= 0:
#                     print(f"[{dino1.name} has been defeated! +45 coins for {dino2.name}! Use them wisely!]\n")
#                     dino2.money += 45
#                     dino1.hp = dino1_initial_hp
#                     dino2.hp = dino2_initial_hp
#                     return
#
#     def show_all_dinosaurs(self):
#         for index, dinosaur in enumerate(self.dinosaurs):
#             print(f"{index+1}. {dinosaur}\n")
#
#
# class Dinosaur:
#     def __init__(self, name, role, hp, damage, attack_speed):
#         self.name = name
#         self.role = role
#         self.hp = hp
#         self.damage = damage
#         self.attack_speed = attack_speed
#         self.kevlar_level = 0
#         self.helmet_level = 0
#         self.gloves_level = 0
#         self.blades_level = 0
#         self.money = 0
#
#     def upgrade_dino(self):
#         if self.kevlar_level == 0:
#             print(f"1. Buy kevlar(+10% hp) - 100 coins")
#         elif self.kevlar_level == 3:
#             print("1. Kevlar is already at the current max level - 3!")
#         else:
#             print(f"1. Upgrade kevlar to level {self.kevlar_level+1}: "
#                   f"{'+15% hp - 150 coins' if self.kevlar_level == 1 else '+20% hp - 200 coins'}")
#
#         if self.helmet_level == 0:
#             print(f"2. Buy helmet(+7% hp) - 70 coins")
#         elif self.helmet_level == 3:
#             print("2. Helmet is already at the current max level - 3!")
#         else:
#             print(f"2. Upgrade helmet to level {self.helmet_level+1}: "
#                   f"{'+10% hp - 100 coins' if self.helmet_level == 1 else '+15% hp - 130 coins'}")
#
#         if self.gloves_level == 0:
#             print(f"3. Buy gloves(+5% attack speed) - 120 coins")
#         elif self.gloves_level == 3:
#             print("3. Gloves are already at the current max level - 3!")
#         else:
#             print(f"3. Upgrade gloves to level {self.gloves_level+1}: "
#                   f"{'+7% attack speed - 150 coins' if self.gloves_level == 1 else '+10% attack speed - 170 coins'}")
#
#         if self.blades_level == 0:
#             print(f"4. Buy blades(+9% damage) - 150 coins")
#         elif self.blades_level == 3:
#             print("4. Blades are already at the current max level - 3!")
#         else:
#             print(f"4. Upgrade blades to level {self.blades_level+1}: "
#                   f"{'+11% damage - 170 coins' if self.blades_level == 1 else '+13% damage - 200 coins'}")
#
#         print("5. Save coins for later")
#
#         option = input("\nEnter the option that you want to upgrade: ")
#         match option:
#             case '1':
#                 self.kevlar_level += 1
#                 if self.kevlar_level == 1:
#                     if self.money >= 100:
#                         self.hp += self.hp*0.1
#                         self.money -= 100
#                     else:
#                         self.kevlar_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.kevlar_level == 2:
#                     if self.money >= 150:
#                         self.hp += self.hp*0.15
#                         self.money -= 150
#                     else:
#                         self.kevlar_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.kevlar_level == 3:
#                     if self.money >= 200:
#                         self.hp += self.hp*0.2
#                         self.money -= 200
#                     else:
#                         self.kevlar_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.kevlar_level == 4:
#                     self.kevlar_level -= 1
#                     return
#                 print("Kevlar successfully upgraded!")
#                 print("\nAfter upgrading:\n")
#                 print(dino_to_upgrade)
#
#             case '2':
#                 self.helmet_level += 1
#                 if self.helmet_level == 1:
#                     if self.money >= 70:
#                         self.hp += self.hp * 0.07
#                         self.money -= 70
#                     else:
#                         self.helmet_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.helmet_level == 2:
#                     if self.money >= 100:
#                         self.hp += self.hp * 0.10
#                         self.money -= 100
#                     else:
#                         self.helmet_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.helmet_level == 3:
#                     if self.money >= 130:
#                         self.hp += self.hp * 0.15
#                         self.money -= 130
#                     else:
#                         self.helmet_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.helmet_level == 4:
#                     self.helmet_level -= 1
#                     return
#                 print("Helmet successfully upgraded!")
#                 print("\nAfter upgrading:\n")
#                 print(dino_to_upgrade)
#
#             case '3':
#                 self.gloves_level += 1
#                 if self.gloves_level == 1:
#                     if self.money >= 120:
#                         self.attack_speed += self.attack_speed * 0.05
#                         self.money -= 120
#                     else:
#                         self.gloves_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.gloves_level == 2:
#                     if self.money >= 150:
#                         self.attack_speed += self.attack_speed * 0.07
#                         self.money -= 150
#                     else:
#                         self.gloves_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.gloves_level == 3:
#                     if self.money >= 170:
#                         self.attack_speed += self.attack_speed * 0.1
#                         self.money -= 170
#                     else:
#                         self.gloves_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.gloves_level == 4:
#                     self.gloves_level -= 1
#                     return
#                 print("Gloves successfully upgraded!")
#                 print("\nAfter upgrading:\n")
#                 print(dino_to_upgrade)
#
#             case '4':
#                 self.blades_level += 1
#                 if self.blades_level == 1:
#                     if self.money >= 150:
#                         self.damage += self.damage * 0.09
#                         self.money -= 150
#                     else:
#                         self.blades_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.blades_level == 2:
#                     if self.money >= 170:
#                         self.damage += self.damage * 0.11
#                         self.money -= 170
#                     else:
#                         self.blades_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.blades_level == 3:
#                     if self.money >= 200:
#                         self.damage += self.damage * 0.13
#                         self.money -= 200
#                     else:
#                         self.blades_level -= 1
#                         print("Not enough coins for this upgrade!")
#                         return
#                 elif self.blades_level == 4:
#                     self.blades_level -= 1
#                     return
#                 print("Blades successfully upgraded!")
#                 print("\nAfter upgrading:\n")
#                 print(dino_to_upgrade)
#
#             case '5':
#                 return
#
#             case _:
#                 print("Invalid option!")
#
#     def __str__(self):
#         return f"Name: {self.name}\nRole: {self.role}\nCoins: {self.money}\n" \
#                f"HP: {self.hp:.2f}\nDamage: {self.damage:.2f}\nAttack Speed: {self.attack_speed:.2f}"
#
#
# class TRex(Dinosaur):
#     def __init__(self):
#         name = "T-Rex"
#         role = "predator"
#         hp = 1400
#         damage = 120
#         attack_speed = 1.0
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Triceratops(Dinosaur):
#     def __init__(self):
#         name = "Triceratops"
#         role = "herbivore"
#         hp = 1800
#         damage = 100
#         attack_speed = 0.6
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Spinosaurus(Dinosaur):
#     def __init__(self):
#         name = "Spinosaurus"
#         role = "predator"
#         hp = 1600
#         damage = 110
#         attack_speed = 0.9
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Velociraptor(Dinosaur):
#     def __init__(self):
#         name = "Velociraptor"
#         role = "predator"
#         hp = 1200
#         damage = 130
#         attack_speed = 1.2
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Stegosaurus(Dinosaur):
#     def __init__(self):
#         name = "Stegosaurus"
#         role = "herbivore"
#         hp = 2200
#         damage = 80
#         attack_speed = 0.5
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Brachiosaurus(Dinosaur):
#     def __init__(self):
#         name = "Brachiosaurus"
#         role = "herbivore"
#         hp = 2600
#         damage = 60
#         attack_speed = 0.4
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# class Diplodoc(Dinosaur):
#     def __init__(self):
#         name = "Diplodoc"
#         role = "herbivore"
#         hp = 2400
#         damage = 70
#         attack_speed = 0.45
#         super().__init__(name, role, hp, damage, attack_speed)
#
#
# def select_dino_menu():
#     while True:
#         print()
#         print("1. Select random dino")
#         print("2. Select a specific dino")
#
#         choice = input("Enter your choice: ")
#         match choice:
#             case "1":
#                 return game.get_random_dino()
#             case "2":
#                 while True:
#                     index = input("Enter the index of the dinosaur you wanna play for: ")
#                     try:
#                         dino_index = int(index)
#                         if 1 <= dino_index <= 7:
#                             return game.get_specific_dino(dino_index)
#                     except ValueError:
#                         print("Enter a numeric in-range value for desired dinosaur's index: ")
#                         index = input("Enter the index of the dinosaur you wanna play for: ")
#                     except Exception:
#                         print("Something went wrong!")
#                         index = input("Enter the index of the dinosaur you wanna play for: ")
#             case _:
#                 print("Invalid choice. Please select a valid option.")
#
#
# if __name__ == "__main__":
#     game = JocVideo()
#
#     player1_dino = None
#     player2_dino = None
#     current_player = 1
#
#     print("Welcome to my Dino Game!")
#     print("Here are are the currently available dinos:\n")
#     game.show_all_dinosaurs()
#
#     while True:
#         print(f"Current player is PLAYER {current_player}!")
#         print("1. Player 1: Select dino")
#         print("2. Player 2: Select dino")
#         print("3. Show all dinosaurs")
#         print("4. Upgrade dino")
#         print("5. Fight")
#         print("6. View your dino")
#         print("7. Toggle current player")
#         print("8. Exit")
#
#         choice = input("Enter your choice: ")
#
#         match choice:
#             case '1':
#                 player1_dino = select_dino_menu()
#                 while True:
#                     if player1_dino != player2_dino:
#                         print(f"\nPlayer 1 selected {player1_dino.name}\n")
#                         print(player1_dino)
#                         print()
#                         break
#                     else:
#                         print("\nPlayers cannot take the same dino!\n")
#                         player1_dino = select_dino_menu()
#             case '2':
#                 player2_dino = select_dino_menu()
#                 while True:
#                     if player2_dino != player1_dino:
#                         print(f"\nPlayer 2 selected {player2_dino.name}\n")
#                         print(player2_dino)
#                         print()
#                         break
#                     else:
#                         print("\nPlayers cannot take the same dino!")
#                         player2_dino = select_dino_menu()
#             case '3':
#                 print()
#                 game.show_all_dinosaurs()
#             case '4':
#                 dino_to_upgrade = player1_dino if current_player == 1 else player2_dino
#                 match dino_to_upgrade:
#                     case None:
#                         print("\nNo dinosaur selected for this player\n")
#                     case _:
#                         print()
#                         dino_to_upgrade.upgrade_dino()
#                         print()
#             case '5':
#                 if player1_dino is None or player2_dino is None:
#                     print("\nBoth players need to select a dinosaur first\n")
#                 else:
#                     print("\nFight starting...\n")
#                     if current_player == 1:
#                         game.fight(player1_dino, player2_dino)
#                     elif current_player == 2:
#                         game.fight(player2_dino, player1_dino)
#             case '6':
#                 dino_to_show = player1_dino if current_player == 1 else player2_dino
#                 match dino_to_show:
#                     case None:
#                         print("\nNo dinosaur selected for this player\n")
#                     case _:
#                         print(f"\n{dino_to_show}\n")
#             case '7':
#                 current_player = 3 - current_player
#                 print()
#             case '8':
#                 print("\nExiting the game! Good luck!")
#                 break
#             case _:
#                 print("\nInvalid choice. Please select a valid option\n")

                                                    # Exercise 3 a)
# from datetime import datetime
# import os
#
# def logare_avansata(func):
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#         func_name = func.__name__
#         arguments = ", ".join([str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()])
#         log_message = f"\nFunction: {func_name}\nTimestamp: {timestamp}\nArguments: {arguments}\n{'-' * 40}"
#         with open("log.txt", "a") as file:
#             if os.path.getsize("log.txt") == 0:
#                 file.write(f"{'-' * 40}")
#             file.write(log_message)
#         return func(*args, **kwargs)
#     return wrapper
#
# @logare_avansata
# def multiply(a, b):
#     print(a*b)
#
# @logare_avansata
# def get_max(list):
#     print(max(list))
#
# @logare_avansata
# def say_hi(name):
#     print(f"Hello {name}")
#
#
# if __name__ == "__main__":
#     say_hi("Valerian")
#     get_max([-34, 99, 13, 25, 19, 33, 22])
#     multiply(8, 1)


                                                    # Exercise 3 b)
# import os, random
#
#
# def limitare_apeluri(func):
#     def wrapper(*args, **kwargs):
#         function_names = {}
#         max_call_times = 5
#         file_path = "call_times.txt"
#
#         if os.path.exists(file_path):
#             with open(file_path, "r") as file:
#                 for line in file:
#                     name, call_times = line.strip().split(" - ")
#                     function_names[name] = int(call_times)
#
#         func_name = func.__name__
#
#         if func_name in function_names:
#             call_times = function_names[func_name]
#             if call_times < max_call_times:
#                 call_times += 1
#                 function_names[func_name] = call_times
#                 with open(file_path, "w") as file:
#                     for name, call_times in function_names.items():
#                         file.write(f"{name} - {call_times}\n")
#                 print(f"Function {func_name} executed {call_times}/{max_call_times} available times! Be careful")
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Maximum amount of calls - {max_call_times} for function {func_name} reached!")
#         else:
#             function_names[func_name] = 1
#             with open(file_path, "a") as file:
#                 file.write(f"{func_name} - 1\n")
#             print(f"Function {func_name} executed for the first time! {max_call_times - 1} executions remained!")
#             return func(*args, **kwargs)
#     return wrapper
#
#
# @limitare_apeluri
# def summ(a, b):
#     print(f"Sum of {a} + {b} = {a+b}\n")
#
#
# @limitare_apeluri
# def get_random_number():
#     print(f"Random generated number = {random.randint(1, 10)}\n")
#
#
# @limitare_apeluri
# def print_python_top():
#     print("Python is really top!")
#     for i in range(random.randint(0, 7)):
#         print_python_top()
#
#
# if __name__ == "__main__":
#     summ(5, 10)
#     get_random_number()
#     print_python_top()


                                                    # Exercise 4 a)
# import os
#
#
# def combina_fisiere(file1_path, file2_path):
#     file_copy_path = "copy.txt"
#
#     if os.path.exists(file1_path) and os.path.exists(file2_path):
#         with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
#             content1 = file1.read()
#             content2 = file2.read()
#
#         combined_content = content1 + "\n\n" + content2
#
#         with open(file_copy_path, "w") as file:
#             file.write(combined_content)
#
#         print("Files copied successfully!")
#     else:
#         print("Both file paths need to be valid and existent!")
#
#
# if __name__ == "__main__":
#     combina_fisiere("log.txt", "call_times.txt")


                                                    # Exercise 4 b)
import os


class AnalizorLog:
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name
        self.function_stats = {}
        self.function_occurrences = {}

    def show_function_stats(self):
        if os.path.exists(self.log_file_name):
            with open(self.log_file_name, "r") as file:
                current_function = None
                timestamp = {}
                arguments = {}
                for line in file:
                    line = line.strip()
                    if line.startswith("Function"):
                        current_function = line.split(": ")[1]
                        self.function_stats[current_function] = {"Timestamp": [], "Arguments": []}
                        self.function_occurrences[current_function] = self.function_occurrences.get(current_function, 0) + 1
                    elif line.startswith("Timestamp"):
                        timestamp_value = line.split(": ")[1]
                        timestamp.setdefault(current_function, []).append(timestamp_value)
                    elif line.startswith("Arguments"):
                        arguments_value = line.split(": ")[1]
                        arguments.setdefault(current_function, []).append(arguments_value)

                    if current_function:
                        self.function_stats[current_function]["Timestamp"] = timestamp.get(current_function)
                        self.function_stats[current_function]["Arguments"] = arguments.get(current_function)

        for function, stat in self.function_stats.items():
            print("Function:", function)
            print("Timestamp:", stat['Timestamp'])
            print("Arguments:", stat['Arguments'])
            print()

        print("Function Occurrences:")
        for function_name, occurrences in self.function_occurrences.items():
            print(f"{function_name}: {occurrences}")


if __name__ == "__main__":
    analizorLog = AnalizorLog("log.txt")
    analizorLog.show_function_stats()
