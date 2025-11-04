import tkinter as tk
from forex_python.converter import CurrencyRates


common_currencies = ["USD","CAD","EUR","GBP","JPY","AUD","CHF","NZD"]



class Converter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry('250x200')


        #Currency created once
        self.c = CurrencyRates()
        
        
        # FROM currency
        self.from_var = tk.StringVar(self.root)
        self.from_var.set("USD")
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=5)

        #TO currency
        self.to_var = tk.StringVar(self.root)  
        self.to_var.set("EUR")
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=5)



        self.amount_label = tk.Label(self.root, text="Amount: ")
        self.amount_label.pack(pady=1)
       


        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)


        self.convert = tk.Button(self.root, text="Convert", command=self.convertCurrency)
        self.convert.pack(pady=5)


        self.result_label = tk.Label(self.root,text="")
        self.result_label.pack(pady=5)

        self.root.mainloop()

        
    def convertCurrency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()  # <-- now it exists
            amount = float(self.amount_entry.get())

            c = CurrencyRates()
            result = c.convert(from_currency, to_currency, amount)

            self.result_label.config(
                text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
            )
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid number")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    Converter()