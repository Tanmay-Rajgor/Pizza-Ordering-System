print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni = 2
pepperoni_m_l = 3
extra_chese = 1
bill = 0

if size == "S":
   bill += 15
elif size == "M":
   bill += 20
else:
   bill += 25

if add_pepperoni == "Y":
      if size == "S":
          bill += 2
      else:
          bill += 3   

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
