class FoodItem:
    def _init_(self, name, quantity, price, discount, stock):
        self.id = None  
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def _init_(self, full_name, phone_number, email, address, password):
        self.id = None  
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class Restaurant:
    def _init_(self):
        self.food_items = []
        self.users = []
        self.orders = []

    # Admin functionalities
    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.id = len(self.food_items) + 1  # Assign the ID
        self.food_items.append(food_item)
        return food_item

    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        food_item = self.get_food_item_by_id(food_id)
        if name:
            food_item.name = name
        if quantity:
            food_item.quantity = quantity
        if price:
            food_item.price = price
        if discount:
            food_item.discount = discount
        if stock:
            food_item.stock = stock

    def get_food_item_by_id(self, food_id):
        for food_item in self.food_items:
            if food_item.id == food_id:
                return food_item
        return None

    def remove_food_item(self, food_id):
        food_item = self.get_food_item_by_id(food_id)
        if food_item:
            self.food_items.remove(food_item)
            return True
        return False

    # User functionalities
    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        user.id = len(self.users) + 1  # Assign the ID
        self.users.append(user)
        return user

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def place_new_order(self, user_id, food_ids):
        user = self.get_user_by_id(user_id)
        if not user:
            return False

        food_items = []
        for food_id in food_ids:
            food_item = self.get_food_item_by_id(food_id)
            if not food_item:
                return False
            food_items.append(food_item)

        order = {"user": user, "food_items": food_items}
        self.orders.append(order)
        return order

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_order_history(self, user_id):
        user = self.get_user_by_id(user_id)


