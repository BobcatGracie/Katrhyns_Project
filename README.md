# Kathryns_Project
Credit Card Budgeting Application

## Installation and Libraries
This application only supports python3!
You will need these standard packages to run the main.py
Most are imported within Python's library, other than matplotlib and flask.

time</br>
os</br>
pandas as pd</br>
flask</br>
matplotlib.pyplot as plt</br>

## Dates
Different date formats have been accounted for and managed in the Class Account Manager, under the plot def.

## Plot Graph Potential Errors
If the plot does not load, it has been coded to simply provide a blank HTML placeholder, so that the application does not crash.

## Walkthrough
After downloading the repo, run the application locally on your computer by going to the Main_File.py, then clicking run and debug.
<img width="3239" height="832" alt="Screenshot 2025-08-04 163722" src="https://github.com/user-attachments/assets/f85473ed-c694-4c79-9b81-38b772da3318" />

After the terminal reads the code, click on the local host.
<img width="2617" height="503" alt="Screenshot 2025-08-04 163743" src="https://github.com/user-attachments/assets/a659b918-a98c-4b07-a9de-0f6fa456c117" />


After a few seconds, the webpage will appear. Here you can add a purchase, which will update the plot, update your target budget, and see your transaction history
![Stand alone we app](https://github.com/user-attachments/assets/67c58001-f832-4c5d-ac08-2cd51c220098)

When adding a budget, simply type in a number to the textbox, click apply, and watch as the graph updates to show your budget line. You can get a relative idea of how close or far you are to exceeding your budget.
<img width="3201" height="1777" alt="Screenshot 2025-08-05 091658" src="https://github.com/user-attachments/assets/51a084a8-a570-4892-9ce6-3b4bf68e4cfc" />



The same can be done when adding a transaction. It will update the balance shown at the top of the screen, add it to the account activity, and add the purchase to the plot.
<img width="3190" height="1772" alt="Screenshot 2025-08-05 091732" src="https://github.com/user-attachments/assets/43746621-0657-467c-99ee-f3e22c253ea9" />

<img width="3201" height="1773" alt="Screenshot 2025-08-05 091848" src="https://github.com/user-attachments/assets/ace755fe-6e76-4d2c-b50a-b3584748e63d" />

## Customization
If you want to use your own financial information, you can clear out the CSV file, or upload your own. Make sure to type in your new file in the Main_File.py. You also have the option to edit the initial balance if you have account information you don’t feel like logging, and it will update the balance. All of this can be found in the Main_File.py. Just be sure to add your CSV file in the data file and delete the old one.
<img width="1438" height="638" alt="Screenshot 2025-08-05 144109" src="https://github.com/user-attachments/assets/faee6dec-8b0e-4896-99b2-ecf534d42f4c" />

## Potential Drawbacks/Future Updates
Sometimes the Application will randomly stop, and all you will need to do is rerun the application. It will save the added transactions, but you will need to go back in and add your budget line. The css also needs some work, but for now it is fine. There is also a small update needed in the account activity. There isn't any reaon to have the time included, so that will be taken in the future, as it's not needed.
