import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import threading

def draw_chart(total_prices_list, cumulative_total_list, product_names):
    plt.plot(total_prices_list, label='Total Prices')
    plt.plot(cumulative_total_list, label='Cumulative Total')
    plt.xlabel('Products')
    plt.ylabel('Price')
    plt.title('ABC Analysis')
    plt.legend()
    plt.xticks(range(len(product_names)), product_names)
    plt.show()

def add_row():
    product_name = tk.StringVar()
    unit_price = tk.StringVar()
    quantity = tk.StringVar()
    total_price = tk.StringVar()
    products.append([product_name, unit_price, quantity, total_price])
    row = len(products)
    ttk.Entry(mainframe, textvariable=product_name).grid(column=0, row=row, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=unit_price).grid(column=1, row=row, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=quantity).grid(column=2, row=row, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=total_price).grid(column=3, row=row, sticky=(tk.W, tk.E))

def calculate():
    try:
        total_prices = [(float(product[1].get()) * float(product[2].get()), product[0].get()) if product[1].get() else (float(product[3].get()), product[0].get()) for product in products]
        total_prices.sort(reverse=True)
        
        total = sum([price for price, _ in total_prices])
        cumulative_total = 0
        data = []
        total_prices_list = []
        cumulative_total_list = []
        product_names = []

        for price, name in total_prices:
            cumulative_total += price
            percentage = (cumulative_total / total) * 100
            if percentage <= 80:
                group = 'A'
            elif percentage <= 95:
                group = 'B'
            else:
                group = 'C'
            data.append([name, price, cumulative_total, percentage, group])
            total_prices_list.append(price)
            cumulative_total_list.append(cumulative_total)
            product_names.append(name)

        threading.Thread(target=draw_chart, args=(total_prices_list, cumulative_total_list, product_names)).start()

        df = pd.DataFrame(data, columns=['Product Name', 'Total Price', 'Cumulative Total', 'Cumulative Percentage', 'Group'])
        new_window = tk.Toplevel()
        text = tk.Text(new_window)
        text.pack()
        text.insert(tk.END, df.to_string(index=False))

    except ValueError:
        print("Please enter valid numbers")

root = tk.Tk()
root.title("ABC Analysis")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
ttk.Label(mainframe, text="Product Name").grid(column=0, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Unit Price").grid(column=1, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Quantity").grid(column=2, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Total Price").grid(column=3, row=0, sticky=(tk.W, tk.E))
products = []
ttk.Button(mainframe, text="Add Row", command=add_row).grid(column=0, row=100, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=100, sticky=(tk.W, tk.E))
add_row()
root.mainloop()
