Budget Wise: Wisely manage your budget

Budget WIse is a web app that will help you keep track of your spending, and calculate your budget. Budget Wise will allow you to log your expenses based on two categories: one is the spending category, and the other is based on need, want, or save. Budget Wise will generate two analytic graphs based on those two categories. Additionally, Budget Wise also allows you to calculate how much your monthly income should go towards saving, want, or need.

Video:
https://www.youtube.com/watch?v=yjwdB4f5tzo&ab_channel=NhiHuynh

Getting started:

1. Clone this repository (or download zip file)

git clone https://github.com/nikki2906/budgetwise.git

2. Go to the app directory

cd path/to/budgetwise

3. Create and activate your virtual environment (optional but recommended!)

○ macOS/Linux:

python3 -m venv venv
. venv/bin/activate

○ Windows (not tested):

py -3 -m venv venv
venv\Scripts\activate
If this works, your command line should now have (venv) in front of each line.

4. Install the app requirements
pip install -r requirements.txt
Run the app!
export FLASK_APP=app
python3 -m flask run

Using Budget Wise:

1. Register for an account! Go to the Registration page and fill out your information. After that, sign in to your account.
2. Log your expense. Provide a description by entering a short description of the thing that you purchased, choose the appropriate categories for your entry.
3. You may revisit ervy expenses that you entered by visiting the history page.
4. By logging your expense for every category, you can access the analytics graphs.
5. Enter your monthly after-tax income into the budget calculator to develop a suggested budget.

Tech:
Frontend: HTML, CSS, Jinja,
Backend: Python, Flask, JavaScript
Database: SQL
Frameworks used: Bootstrap (frontend)

