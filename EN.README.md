# ABC Analysis Application
# Introduction
ABC Analysis is an inventory categorization method widely used in materials management. It is also known as Selective Inventory Control. Items in the inventory are classified into three categories: A, B, and C, based on their importance. 'A' items are considered to be the most important, 'B' items are less important and 'C' items have the least importance.

This application is designed to perform ABC Analysis on a given set of products and their respective prices and quantities. It uses a graphical user interface (GUI) built with the tkinter library and generates charts using matplotlib.

# How to use the application
When the application is launched, you'll see a window with four columns labeled "Product Name", "Unit Price", "Quantity", and "Total Price", as well as two buttons labeled "Add Row" and "Calculate".

To enter data for a product, fill in the appropriate fields in the first row:

# Product Name: Enter the name of the product.
# Unit Price: Enter the unit price of the product.
# Quantity: Enter the quantity of the product.
# Total Price: You can either enter the total price directly or leave it blank. If left blank, it will be calculated as Unit Price * Quantity.
To add more products, click the "Add Row" button. This will create a new row for you to enter additional product information.

After you have entered all the product information, click the "Calculate" button. The application will perform ABC Analysis and:

A chart will be displayed, showing the total prices and cumulative total of the products.
A new window will pop up with a table showing the product name, total price, cumulative total, cumulative percentage, and group (A, B, or C) for each product.
You can close the application by closing the main window.

# Dependencies
Python
pandas
matplotlib
tkinter
# Purpose
This application is useful for inventory managers, small business owners, and anyone who needs to perform ABC Analysis on a set of products. It helps in understanding which products are contributing the most to the total value and helps in making informed decisions regarding inventory control and management.

Please note that this application is for educational purposes and may require additional features and validation for professional use.
