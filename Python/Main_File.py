import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
#Copied and edited from HCI 574 lecture 36
from flask import Flask, render_template, request, redirect, url_for # now also import the render template class
app = Flask(__name__)


CSV_FILE = 'Transactions.csv'
INITIAL_BALANCE = 100.0


class AccountManager:
    def __init__(self,initial_balance = INITIAL_BALANCE,csv_file = CSV_FILE):
            self.csv_file = csv_file
            self.initial_balance = initial_balance
            #self.activities = self._load_activities()
            self.df = self.load_file()


    def load_file(self):
            """Loads data from the CSV file"""
            if os.path.exists(self.csv_file):
                try:
                    df = pd.read_csv(self.csv_file)
                    print(f"File exists as {self.csv_file}")
                    return df
                except pd.errors.EmptyDataError:        #I did look this up on google but it seems to do what I'm wanting
                    print("Error: The file is empty.")
                    return None
            else:
                print(f"{self.csv_file} File not found")
                return None
            
    def __str__(self):
         s = (f"Database: {self.csv_file}, Initial Balance: {self.initial_balance}\n")
         if self.df is not None:
              s += ("DataFrame contents:\n")
              s += self.df.to_string()
              return s

    def update_balance(self):
        """Updates the current balance based on user activity, 
        after initial balance. Should update after loading"""
        current_balance = self.initial_balance
        #figure out how add the purhcase amount rows from CSV file
        for _, row in self.activities.iterrows():
            if row['Type'] =='Purchase':
                current_balance -=row['Amount']
            elif row['Type'] =='Refund':
                current_balance += row['Amount']
        return current_balance

    def get_balance(self):
        """Gives user their current balance."""

    def get_activity(self):
        """Gives user their activity."""

    def plot(self):
        """Plots the balance over time."""
        # line plot amount in self.df over time using matplotlib
        # only plot purchase and color by catagory
        #Bar chart or graph.....lookup what is most popular
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['Date'], self.df['Amount'], marker='o', linestyle='-')
        plt.title('Balance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        # CH you will need to figure out how to integrate this with Flask to display the plot in the web app
        # You could save the plot to a file and then render it in a img tag in the HTML template
        plot_path = 'static/plot.png'  # Save the plot to a static directory (subfolder in your Flask app, such as templates)       
        plt.savefig(plot_path)
        plt.close()


accman = AccountManager()


@app.route("/")  
def index():
    html_str = render_template('index.html', title="Landing Page") # title will be inlined in {{ title }}
    print(html_str) # DEBUG
    return html_str  # give it to the browser to display the inline page

app.run(debug=False, port=8080) 


@app.route('/add_transaction', methods=['POST'])
def add_activity(self, type, catagory, amount):
        """Adds new activity and will sort what type of activity it is(refund or charge),
        catagory(grocery/transportation), and the amount."""
        if request.method =='POST':
            transaction_type = request.form['transaction_type']
            store = request.form['store']
            amount = request.form['amount']
            date = request.form['date']

            #Append data to CSV file
            #I got this from the internet
            try:
                with open(CSV_FILE, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([transaction_type, store, amount, date])

                return render_template('index.html', message="Transaction added successfully!", message_type="success")
            except Exception as e:
                return render_template('index.html', message=f"Error adding transaction: {e}", message_type="error")

@app.route('/purchase', methods=['POST']))
def purchase(self, amount, catagory):
        """Adds purchase activity and subtracts from the balance. Hopefully warns & 
        denies the purchase if the user doesn't have the balance to cover it,"""

        try:
            amount = float(request.form['amount'])
            category = request.form['catagory']

            if self.balance - amount < 0:
                print("Insufficient funds. Your balance will not cover this transaction.")
                return False
        except ValueError:
            print("Please enter a valid number")

        self.balance -= amount

        #This part I got from Google Gemini. It records a purchase after the balance is updated
        self._add_activity('Purchase', category, amount)
        self.activities.loc[self.activities.index[-1], 'BalanceAfter'] = self.balance
        self._save_activities()
        return True, f"Purchased ${amount:.2f} ({category}). New balance: ${self.balance:.2f}"

#need a def for handling str + floats for consistency
#maybe defs for UI(menu, tables, charts, viewing activity)