Motivations
Background
Being a student in high school, I never learn about how to create good budgeting habits. I worked a part-time job during high school, yet as someone who did not know how to budget well, I ended up spending $100 to $200 a week on unnecessary expenses. Not until my senior year, I took a class financial literary class where I learned about the 50/30/20 budget rule which completely changed my mindset about budgeting. I usually keep track of my expenses using a pen and paper, but I noticed that it was not very efficient as it took a long time to write down everything, and unorganized as I sometimes forgot to log my expenses in.

Why Budget Wise?
I though it was time for a digital solution t help me be more efficient with my money. I wanted to create a tool to help people to easily access to financial planning resources. I also realized that there are over 65 mmllion people in the US who regularly use a 50/30/20 budget rule to mangage their money. Therefore, I created the calculator function to make it easy for people to create a budget plan right inside Budget Wise. Budget Wise is different from other exissitng application because it allows you to track your expenses based on the 50/30/20 budget rule which specifically designed to help individuals who were living on a tight budget.

Bootstrap
I use Bootstrap to build and style for Budget Wise. Bootstrap is an open-source front-end  framework that make sit simple and fast for developers to create great-looking web applications.

Flask & Python
I use Flask and Python to create Slab's backend. I used Flask because flask is a lightweight python web framework that makes it easy to create dynamic websites. Flash also uses Jinja2 as a templating engine in order to easily customize the font end of the website.

SQL
I use SQL to query the database and store user information. Using SQL allows for quick retrieval of data from a local base. SQL also allows for extremely easy and effective table insert, search, update, and delete database records.

JavaScript
I use JavaScript to communicate with HTML elements for the calculator portion. By using JavaScript, it allows me to add interactivity to the page by allowing users to use various types of controls such as buttons, and drop-down selections.

Google Charts API
I use Google Charts for the analysis of the user’s inputs. Google Charts is a charing library built entirely in JavaScript that adds interactive charting functionality to web applications. Google Charts are easy to learn and interactive because it works on all modern browsers. Most importantly, it can read from the SQL databases and auto-update.

A tour inside of BudgetWise
Budget Wise’s Database
I use SQL for my database needs, so all all my tables are represented and stored in budgetwise.db. BudgetWise’s database consists of two tables, on storing Users, and on storing Spendings. Spendings is the sub-table of Users because it allows any given user to enter unlimited inputs, as well as allows them to edit and input database for analysis. Unique IDs are issued to Users and Spendings which serve as primary keys in their respective databases as well as to enture that they can browse only their own spendings. Spendings are connected with the User ID, so that the system can identity the expenses that a particular has imputed.
Within Spendings are

Registration
Registration is created with Flask, SQL, with some Bootstrap for the form format and styling. I use HTML to create a registration form, and use Flask to render a registration form and set constraints on the user input such as providing a valid username/ password, the password confirmation matching, and requiring users’ passwords to have some number of letters, numbers, and/or symbols. When is the form is submitted, the inputs is obtained from the table and a new user is built with the provided username, and password. The new user information is added to the Users table. Finally, the user is redirected to their new account's login page.

Login
Login is created with Flask, SQL, with some Bootstrap for the form format and styling. I use HTML to create a registration form, and use Flask to render a registration form and set constraints on the user input such as providing a valid username/ password. When the form is validated and is sent via a POST request, I use SQL to check my users table to see if the user exists, and then log them in.

Log Expenses
When the user goes to log their expenses, they will be prompted to enter the description, amount, and select a category from spending category 1, make another selection from the spending category 2. I decided to implemented the submission like this because it is not only makes it simple for the user but also simplifies the interpretation process on the backend. When the log is submitted and the data has been extracted from it, a new spending is generated and added to the database.

History
Users can access the spendings that they entered, therefore the history allows the users to see their spendings neatly presented in an easy to follow format. Budget Wise’s history is dynamic because when the user input new data for the same category, the amount will be updated by adding up the old amount with the new amount based on a particular category.

Analytics
Since the log expenses are created with Flask and SQL for the purpose of simplicity and ease of use which allows me to set constraints to the users, for example, enforce enter inputs for all categories to ensure that analytics are accurately provided. When obtaining enough data, the analytics graph will be produced automatically based on the data that is passed in from the database. Analytics is created using Google Charts API because it is customizable based on the input data.

Calculator
To find out the suggested budget, the calculator will take input from the user which is the amount which is the amount of their weekly/ monthly income, and asks them to choose the category they want to calculate (save, want, or need). According to the input from the user, the budget calculator will calculate the suggested budget and then print it. In the Javascript section, the calculator processing the taken input, and after calculating, the respective output is printed.

Styling
I designed Budget Wise’s logo, which appears in the navbar and as the favicon. For the main homepage, Budget Wise incorporates illustrations created by @denayune. For the registration and login page, Budget Wise incorporates illustrations created by @Marta Shershen. Slab uses the gradient button hover to add more fun and dynamic to the webpage.


