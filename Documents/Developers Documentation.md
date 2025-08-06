# OVERVIEW

This budgeting app allows users to look at their spending, see what their current spending is, look at their transaction history, add transactions(purchases and refunds), and also allows them to see their current balance in real time with a chart showing their balance over time.

Using Flask and a local host, users are able to easily download the repo and start using the test data provided, or they can upload their own CSV’s/Initial Balance.

After downloading the repo, you may run the app just to see the layout and all the things you can add by going to the Main_file.py and running the app on a local server. If you want to use your own financial information, you can clear out the CSV file, or upload your own. Make sure to type in your new file in the Main_File.py. You also have the option to edit the initial balance if you have account information you don’t feel like logging, and it will update the balance. 

# MAIN INTERACTIONS
## Adding Activity
The user has the ability to make purchases/refunds(which will be used to calculate their balance), indicate what business establishment they got the item/service from, input the dollar amount in xx.yy format, select the date(sorts the plot by date), and select a category. This helps users organize their transaction to see what money is being used, where it's going, how much is being used, when it was obtained, and what to best categorize their expenses.

## Adding a Budget
In the event users want to stay under a certain budget, they can update it under the Set Your Budget Widget. This way it will add a red line to the plot, and allow users to get a quick and easy glance at how close their spending is to the budget line. The budget can always be updated. Plot Chart of Balance Over Time with each added transaction, and using existing data, a plot.png will appear on the page to show users how much they spent on any given day. This chart rises with the more purchases they make. It also shows a budget line if the user wants to set one.

## Viewing the Account Activity 
At the bottom of the page, users can see all updated account activity including the categorizations from adding activity.

# CODE WALKTHROUGH & ISSUES
## Main_File.Py
The main code that runs this application is the Class Account Manager. Besides the basics needed to run a flask application, it involves other defs needed to successfully run the application. The first one is for making sure that the CSV file loads and is read correctly, with some error parameters in the event a user uploads a file that doesn’t work.
Updating the balance ensures that whenever the application is loading, it has the correct balance number stored(it does not show). Purchases add to the balance while refunds subtract from the balance. Get balance basically shows the user the current balance they have after the application loads and has updated the balance from previous use.
Getting the activity shows users their transaction history. Plot is used to plot the individual transactions onto a chart that users can quickly scan. It saves the plot as a PNG which is then updated to show the most recent history. It also has error parameters so that the website doesn’t crash if the png file will not load. It also makes sure that any date format will work when adding new information, and shows up on the plot in chronological order. Using the initial balance, purchase, and refunds, it rises with purchases and declines with refunds. This is also where users can set their budget which is indicated by a red dotted line. Lastly there are the app.routes to link the Python to the index.html. For fixes, it will look much better if the time were not included when it shows the account activity. I never got around to figuring out how to fix it, but it's a smaller fix that doesn’t affect the performance of the application.

## index.html
This can be found in the templates folder and has the code for the basic structure of the webpage. The header is spread across the whole page, while the main body is split into a two column layout. The left column contains the budget setting while the right container holds everything else. The new transaction section is directly tied to the def add_activitey in the Main_File.Py. So if you want to add or take away anything, make sure these are correctly named for storage. The balance over time html section also correlates with def index in the Main_file, and makes sure the plot gets shown properly with each update. Last, the account activity section works with the Python file def get_activitey. 

## style.css
For the style sheet I implemented Helvetica as the main font-family. The header is pretty self explanatory, but I did add a small rectangle to help divide the contents of the page, using a <div> in the HTML file. This is technically not good practice, so it will need to be updated in the future. I also had a single line divider to separate the two columns, however it created a new random line in the middle of the page. This is partially due to the rectangle, but is in the CSS. It needs troubleshooting and fixing if you would like to implement that instead of the border around the right column. The last fix that needs to be made is in the #new-transaction form . Each new transaction box is its own entity, and the css is aligning them in the middle vertically with a row. Because there isn’t any text above the submit button, it is aligning itself in the middle. Other than these few problems, the rest of the CSS is self explanatory and still works fine for the project.

# FUTURE WORK
While I did reach my MVP goals, one big addition I would like to have is being able to filter through the types of transactions(groceries, transportation, entertainment, etc) and show users the categories of biggest spending vs lowest spending.
Another thing I briefly thought about was being able to filter by time periods, so users can go back and look at what they spent during specific time periods in the past. 
For inefficiencies, the CSS needs major work as it's not up to standard, and there are better ways to implement what I want, so that just deals with needing more time to think out. It would also be cool if I could make the plot interactive, which would require more knowledge for me to code, but seems like a very attainable goal by using seaborn.
