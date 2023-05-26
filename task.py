import requests
import json

def main():
    while True:
        print("This is a MENU, please enter a number for what you are looking for:")
        print("1. Carts")
        print("2. Products")
        print("3. Users")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                cart_id = input("Welcome to the carts department! Please enter cart ID (or 0 for all entries): ")
                if cart_id == "0":
                    # Using fetch API to retrieve and display all carts
                    fetch_url = 'https://dummyjson.com/carts'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        carts = fetch_response.json()
                        print(json.dumps(carts, indent=2))
                    else:
                        print(f"Failed to fetch carts. Status code: {fetch_response.status_code}")
                    break
                else:
                    # Using fetch API to retrieve and display a specific cart by ID
                    fetch_url = f'https://dummyjson.com/carts/{cart_id}'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        cart = fetch_response.json()
                        print(json.dumps(cart, indent=2))
                    else:
                        print(f"Cart not found. Status code: {fetch_response.status_code}")

        elif choice == "2":
            while True:
                product_id = input("Welcome to the products department! Please enter product ID (or 0 for all entries): ")
                if product_id == "0":
                    fetch_url = 'https://dummyjson.com/products'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        products = fetch_response.json()
                        print(json.dumps(products, indent=2))
                    else:
                        print(f"Failed to fetch products. Status code: {fetch_response.status_code}")
                    break
                else:
                    fetch_url = f'https://dummyjson.com/products/{product_id}'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        product = fetch_response.json()
                        print(json.dumps(product, indent=2))
                    else:
                        print(f"Product not found. Status code: {fetch_response.status_code}")

        elif choice == "3":
            while True:
                user_id = input("Welcome to the users department! Please enter user ID (or 0 for all entries): ")
                if user_id == "0":
                    fetch_url = 'https://dummyjson.com/users'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        users = fetch_response.json()
                        print(json.dumps(users, indent=2))
                    else:
                        print(f"Failed to fetch users. Status code: {fetch_response.status_code}")
                    break
                else:
                    fetch_url = f'https://dummyjson.com/users/{user_id}'
                    fetch_response = requests.get(fetch_url)
                    if fetch_response.status_code == 200:
                        user = fetch_response.json()
                        print(json.dumps(user, indent=2))
                    else:
                        print(f"User not found. Status code: {fetch_response.status_code}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
