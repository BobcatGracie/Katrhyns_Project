import os
import pandas as pd
import matplotlib.pyplot as plt

#Copied and edited from HCI 574 lecture 36
from flask import Flask, render_template, request, redirect, url_for # now also import the render template class
app = Flask(__name__)


# CH usually all the flask stuff is done at the end so I moved it there
CSV_FILE = 'Transactions.csv'
INITIAL_BALANCE = 100.0


class AccountManager:
    def __init__(self,initial_balance = INITIAL_BALANCE,csv_file = CSV_FILE):
            self.csv_file = csv_file
            self.initial_balance = initial_balance
            #self.activities = self._load_activities() # CH this was not defined, so I commented it out 
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

    # CH I don;t think you need this method if you save the dataframe to csv after each activity
    # (it's just one line, so using a method isn't really needed)
    def save(self):
        """Saves the current data and activity"""
        #Not sure if this is right???
        #self.activities.to_csv(self.csv_file, index=False)


    def update_balance(self):
        """Updates the current balance based on user activity, 
        after initial balance. Should update after loading"""
        
        # CH if the initial csv exists add the amount up otherwise (csv did exist but wad empty) use the initial balance
        if self.df is not None and not self.df.empty:   
            self.initial_balance = self.df['Amount'].sum()
        else:
            self.initial_balance = INITIAL_BALANCE

        print(f"Balance: {self.initial_balance}")
        

    # is this needed? add_actity should already civer this (???)
    def purchase(self, amount, catagory):
        """Adds purchase activity ans subtracts from the balance. Hopefully warns & 
        denies the purchase if the user doesn't have the balance to cover it,"""


    def get_balance(self):
        """Gives user their current balance."""

    def get_activity(self):
        """Gives user their activity."""

    def plot(self):
        """Plots the balance over time."""
       # line plot the amount in self.df over time using matplotlib
       # only plot purchase and color by category
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['Date'], self.df['Amount'], marker='o', linestyle='-')
        plt.title('Balance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        #plt.show() # DEBUG :  CH you will need to figure out how to integrate this with Flask to display the plot in the web app
        # You could save the plot to a file and then render it in a img tag in the HTML template
        plot_path = 'static/plot.png'  # Save the plot to a static directory (subfolder in your Flask app, such as templates)       
        plt.savefig(plot_path)
        plt.close()
        #


#need a def for handling str + floats for consistency
#maybe defs for UI(menu, tables, charts, viewing activity)

# CH using a gobal variable for the account manager, which assumes there is only one user
# otherwise it will be shared across all users (browsers)
accman = AccountManager()  # create an instance of AccountManager
# the alternative is to create an instance of AccountManager in each route that needs it




# CH usually all the flask stuff is done at the end so I moved it there
@app.route("/")  
def index():
    plot_path = accman.plot()
    html_str = render_template('index_CH.html', title="Landing Page",  plot_url=plot_path) # title and plot file will be inlined in {{ title }}

    #print(html_str) # DEBUG
    return html_str  # give it to the browser to display the inline page

@app.route('/add_transaction', methods=['POST'])  # CH if you only allow POST why test for it later?
def add_activity(): # CH no arg here b/c you get their data from the GUI and accman
    """Adds new activity and will sort what type of activity it is(refund or charge),
    catagory(grocery/transportation), and the amount."""
    transaction_type = request.form['transaction_type']
    store = request.form['Buisness Establishment']  # CH changed from 'store' to 'Buisness Establishment' to match the HTML form (typo, BTW)
    amount = request.form['amount']
    date = request.form['date']

    # add the transaction to the DataFrame
    # Date,Description,Amount,Type,Category 
    new_transaction = { # can be in any order but must match the Above CSV header
        'Type': transaction_type,
        'Description': store,
        'Amount': float(amount),
        'Date': date,  # BTW has different format that Date in csv file
        'Category': "yes"   
    }   
    print(accman.df)
    # "add" new row at the bottom of the DataFrame
    accman.df = pd.concat([accman.df, pd.DataFrame([new_transaction])], ignore_index=True)
    print("\n\n", accman.df)
    # save the updated DataFrame to the CSV file
    accman.df.to_csv(accman.csv_file, index=False)

    # update the balance
    accman.update_balance()

    return redirect(url_for('index'))

app.run(debug=False, port=8080) 
