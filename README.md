# Welcome to Tomtuhtomtom's Flashcard App

This app allows users to register, login and create flashcards for study purposes.  A traditional flashcard has a question written on one side and an answer written on the other side in which people can test themselves by looking at the question without being able to see the solution until the card is flipped over.  In this app, the user will be able to input questions and answers and when ready to test themselves, the questions will be displayed with the solutions hidden until the user is ready to display the answer.  This app followed the Real Python tutorial with some additional features and styling adjustments.  Go to https://realpython.com/django-flashcards-app/ for Real Python's tutorial.

# Getting started

Installation steps:
1. Open your terminal

For Windows
Click Start and search for "Command Prompt." You can also press Ctrl + r on your keyboard, type "cmd" and then click OK.

For MacOS
Open Launchpad and search for terminal. You can also press command⌘ + space on your keyboard and search for "terminal."

For Linux
The terminal will be accessed differently depending on which interface you use. Check out Ubuntu's Using the Terminal page for the various ways to access the terminal. https://help.ubuntu.com/community/UsingTheTerminal?action=show&redirect=BasicCommands

2.  Make a directory to copy the app to your computer

Once you are in the terminal, you will use the command mkdir to make a directory.  Navigate to where you would like to make the directory type mkdir then the name of the directory.  For example: mkdir name_of_directory

3. Make sure Git is installed on your computer

Follow github's insallation guides for intalling Git here: https://github.com/git-guides/install-git

4. Go to the Github website containing the app

If you are viewing this page, more than likely you are at https://github.com/Momentum-Team-14/django-duplex-Tomtuhtomtom if not, you can click the link to find the source code for the app. 

5. Make a clone of the app

From there, you will be able to click on the green code button and clone a copy for yourself by clicking on the button next to the url that looks like two boxes with on one top of the other.

6. Copy the app to your directory

Back in the terminal and in your directory type git clone then paste the copied url for the app.  It should look like this: git clone https://github.com/Momentum-Team-14/django-duplex-Tomtuhtomtom.git Once you've cloned the project you should see a new directory called django-duplex-Tomtuhtomtom in the directory you made. Go into this directory.

7. Install pip, pipenv, python, and django

There are several options for virtual environments.  We recommend installing pip and pipenv to handle the virtual environment needed to run this app.  

Go to https://pip.pypa.io/en/stable/installation/ for intructions on installing pip.

Go to https://pypi.org/project/pipenv/ for installation and more information about pipenv.

Go to https://www.python.org/downloads/ for information and guides for python.

Go to https://docs.djangoproject.com/en/4.1/topics/install/ for intructions on installing django.

8. Start the virtual environment and migrate the database

Once everthing in step 7 is installed, you should be able to launch the virtual environment from your terminal propmt by typing: pipenv shell  

You'll need to ensure that database is configured properly in order for the app to function correctly.  You should be in the right directory but you may need to ensure that you are in the directory that contains the file manage.py.  Run the following commands in your terminal: 

python manage.py makemigrations
python manage.py migrate

This first command should show if there is anything to migrate and prepares the migratation and if the migrations are successful, the second command should result in messages with OK at the end of them.

9. Run the local server

If steps 1 through 8 were successful, you should be ready to launch the app by running the local server.  You do this by typing into your terminal: python manage.py runserver

If successful, you will get a message stating that it started the development server, the expected address will be http://127.0.0.1:8000/ Enter this address into your browser address bar and the application should load

# How to use the app

Once the app has loaded, you should see a page asking you to login.  If you don't have an account, don't worry, when you click on login, there will be an option to register down at the bottom of the page.  Click on register and fill out the information in the form and once you've registered, it will automatically take you back to the home page showing you the full contents of the app.  The login conveniently becomes a link to logout when you are finished. 

There will be some links underneath the welcome message displaying your username letting you know you are logged in.  The top link will say All Cards and there are three boxes below that link.  This app uses the Leitner System for studing with flashcards and you can get more information provided by Mindedge here: https://www.mindedge.com/learning-science/the-leitner-system-how-does-it-work/

The main content of the page will show all of the cards that have been created in the app so first, we need to create some cards.  There is a link underneath the header that says "All Cards" for you to create a card.  Click this link and it will bring up a form in which you type in the question, the answer, the subject category and it's recommended that all cards are placed in box 1 when created so 1 will show automatically but you have the ability to change the box if desired. Once you have filled out all the information and click the Save Card button, it will show the card in the main page.  You will also notice that the number of cards in the box links at the top of the page has adjusted accordingly.  

Once you have created some cards and are ready to start studying, simply click on the box link at the top of the page you would like to study and it will randomly choose one of the cards in the box and display all the information except for the answer.  You should see what box you are in, how many cards are left in that particular box, the subject category and the question.  Underneath the question, you will notice a triangle and the words "Show Answer" need to it.  When you are ready to check the answer, click on triangle or the words and the answer will appear below.  If you guessed correctly, good job! Click on the button that says "I got it right!" and the card will automatically be placed in the next box up so cards in box 1 that are guessed correctly will go to box 2 and from box 2 will go to box 3.  If you study using box 3, correct answered cards will stay in box 3.  If you guessed incorrectly, you'll want to click the button that says "I got it wrong!" and the card will move back to box 1 no matter which box it was in.

Now that you've got the hang of creating cards and how to use them to study, what if you want to change the card or get rid of it altogether?  If so, click the All Cards link at the top of the page at any time to go back to the list of all the cards and under each card answer, there are two links.  One link to edit the card and one to delete it.  If you click the edit card, it will show open a form showing you the current information and simply change the information that you would like to change and click "Save Card."  The Cancel link under the save button will take you back to the All Cards page.  If you click the delete card link, it will open a page asking you if you are sure along with a button to confirm and an option to cancel if you clicked delete by mistake.  

That's it!  You are ready to explore the app and use it to make as many cards as you'd like to help you study.  This is the first version of the app.  Many more features, styles, options to come!

