# Define the menu of a resturent
menu = {
    'Pasta': 180,
    'Pizza': 300,
    'Mixed Salad': 160,
    'Coffee': 140,
    'Tea': 120,
    'Ice Cream': 200,
    'Bhuna Gosht': 350,
    'Chicken Biryani': 250,
    'Mutton Korma': 400,
    'Vegetable Curry': 220,
    'Naan': 40,
    'Roti': 30,
    'Lassi': 100,
    'Mango Shake': 150,
    'Chocolate Shake': 180,
    'Fruit Salad': 120,
    'Grilled Chicken': 320,
    'Fish Curry': 280,
    'Paneer Butter Masala': 240,
    'Dal Makhani': 200,
    'Gulab Jamun': 90,
    'Ras Malai': 110,
    'Kheer': 130,
    'Samosa': 50,
    'Pakora': 60,
    'Chaat': 80,
    'Pav Bhaji': 150,
    'Mutton Rogan Josh': 450,
    'Chicken Tikka Masala': 300,
    'Vegetable Biryani': 200,
    'Butter Chicken': 350,
    'Shahi Paneer': 280,
    'Tandoori Murgh': 320,
    'Dal Makhani': 200,
    'Special Gulab Jamun': 90,
    'Special Ras Malai': 110,
    'Special Kheer': 130,
    'Chicken Samosa': 50,
    'Vegetable Pakora': 60,
    'Fushka': 80,
    'Sea food Biryani': 300,
    'Mutton Biryani': 350,
    'Brownies': 150,
    'Cheesecake': 180,
    'Chocolate Mousse': 200,
    'Vanilla Ice Cream': 120,
    'Strawberry Ice Cream': 130,
    'Mango Ice Cream': 140,
    'Pineapple Ice Cream': 150,
    'Lava Cake With Ice Cream': 250,
    'Tiramisu': 220,
    'Pista Kulfi': 160,
    'Rose Kulfi': 150,
    'Kesar Kulfi': 170,
    'Badam Kulfi': 180,
    'Gajar Halwa': 100,
    'Moong Dal Halwa': 120,
    'Suji Halwa': 90,
    'Lava Cake With Ice Cream': 250,
    'Chicken Carnival Platter': 500,
    'Dynamic Duo Platter': 450,
    'Veggie Delight Platter': 400,
    'Seafood Sensation Platter': 550,
    'Mutton Feast Platter': 600,
    'Mix Grilled Platter': 480,
    'Tandoori Platter': 520,
    'RIB Eye Steak': 700,
    'Filet Mignon': 800,
    'New York Strip': 750,
    'Porterhouse Steak': 850,
    'T-Bone Steak': 900,
    'Tomahawk Steak': 950,
    'Ribeye Cap Steak': 1000,
    'Flat Iron Steak': 650,
    'T Bone Steak': 900,

}

#Greeting message
print("Welcome to SIAMÉ! Here is our menu:")

# Display the menu
for item, price in menu.items():
    print(f"{item}: {price} BDT")


#Order Total
order_total = 0

item_1 = input("Enter the name of item you would like to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} added to your order.")
else:
    print(f"Order item  {item_1} is not available yet.")

another_order = input("Do you want to add another item? (yes/no): ")

if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} added to your order.")
    else:
        print(f"Order item  {item_2} is not available yet.")

print(f"The total amount of items to pay is: {order_total} BDT")


#Payment method
payment_method = input("Please select a payment method (cash/card/mobile): ")
if payment_method == "cash":
    print("You have selected cash payment. Please pay the amount to the cashier.")
elif payment_method == "card":
    print("You have selected card payment. Please swipe your card at the terminal.")
elif payment_method == "mobile":
    print("You have selected mobile payment. Please use your mobile app to complete the transaction.")
else:
    print("Invalid payment method selected. Please choose cash, card, or mobile.")

