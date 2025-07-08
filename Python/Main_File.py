import csv
import os
import pandas as pd

#Copied and edited from HCI 574 lecture 36
from flask import Flask, render_template, request, redirect, url_for # now also import the render template class
app = Flask(__name__)

@app.route("/")  
def index():
    html_str = render_template('index.html', title="Landing Page") # title will be inlined in {{ title }}
    print(html_str) # DEBUG
    return html_str  # give it to the browser to display the inline page

app.run(debug=False, port=8080) 



CSV_FILE = 'Transactions.csv'
INITIAL_BALANCE = 100.0


class AccountManager:
    def __init__(self,initial_balance = INITIAL_BALANCE,csv_file = CSV_FILE):
            self.csv_file = csv_file
            self.initial_balance = initial_balance
            self.activities = self._load_activities()
            self.df = self.load_file()


    def load_file(self):
            """Loads data from the CSV file"""
            if os.path.exists(self.csv_file):
                try:
                    df = pd.read_csv(self.csv_file)
                    print(f"File exists as {self.csv_file}")
                    return df
                except pd.errors.EmptyDataError:        #I did look this except up on google but it seems to do what I'm wanting
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


    def save(self):
        """Saves the current data and activity"""
        #Not sure if this is right???
        self.activities.to_csv(self.csv_file, index=False)

    def update_balance(self):
        """Updates the current balance based on user activity, 
        after initial balance. Should update after loading"""
        current_balance = self.initial_balance
        #figure out how add the purhcase amount rows from CSV file
        
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
                    writer.writerow([transaction_type, item, amount, date])

                return render_template('index.html', message="Transaction added successfully!", message_type="success")
            except Exception as e:
                return render_template('index.html', message=f"Error adding transaction: {e}", message_type="error")

    def purchase(self, amount, catagory):
        """Adds purchase activity ans subtracts from the balance. Hopefully warns & 
        denies the purchase if the user doesn't have the balance to cover it,"""


    def get_balance(self):
        """Gives user their current balance."""

    def get_activity(self):
        """Gives user their activity."""

    def plot(self):
        """Plots the balance over time."""
        #Bar chart or graph.....lookup what is most popular

#need a def for handling str + floats for consistency
#maybe defs for UI(menu, tables, charts, viewing activity)
def main():
    """Runs the Account Manager for users to input data."""