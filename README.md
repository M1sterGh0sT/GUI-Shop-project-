# Grocery Store Billing Application

This repository contains a Python implementation of a **Grocery Store Billing Application** using Tkinter. The application allows users to add various grocery items to their cart, calculates the total cost, and generates a bill for the purchased items. It is designed to simulate a simple billing system for a grocery store.

## File Structure

- `Grocery Store Billing.py`: The main Python script containing the implementation of the Grocery Store Billing Application.
- `README.md`: This file, providing an overview and description of the project.

## Classes and Functions

### `Project` Class

The `Project` class encapsulates all the functionalities required for the Grocery Store Billing Application.

#### `__init__(self)`

Initializes the `Project` class with the following attributes and methods:
- `root`: The main Tkinter window.
- `total_amount`: Variable to store the total amount of the bill.
- `items`: Dictionary to store the items and their details.
- `initialize_gui()`: Method to set up the GUI components.

#### `initialize_gui(self)`

Sets up the graphical user interface (GUI) for the application, including:
- Creating frames
- Adding labels, entry fields, and buttons
- Configuring the layout

#### `add_item(self, category, item, price, weight)`

Adds an item to the cart. Parameters include:
- `category`: Category of the item (e.g., Fruits, Vegetables)
- `item`: Name of the item
- `price`: Price per unit weight of the item
- `weight`: Weight of the item being purchased

#### `calculate_total(self)`

Calculates the total amount of the bill by summing up the cost of all items in the cart.

#### `generate_bill(self)`

Generates a detailed bill displaying all the items purchased, their quantities, prices, and the total amount.

#### `clear_cart(self)`

Clears all items from the cart and resets the total amount.

## Usage

1. **Install the required dependencies:**
   Ensure you have Python and Tkinter installed on your system.

2. **Run the application:**
   Execute the `Grocery Store Billing.py` script to launch the application.

3. **Interact with the GUI:**
   Use the GUI to add items to your cart, specify their weight, and generate a bill.

## Example

To add an item to the cart, specify the category, item name, price, and weight, and then click the "Add to Cart" button. The application will calculate the total amount and generate a detailed bill.

```python
project = Project()
project.add_item('Fruits', 'Apple', 3.0, 2.5)
project.add_item('Vegetables', 'Carrot', 1.5, 1.0)
project.calculate_total()
project.generate_bill()
