Intro & Objectives
In this project you will put together concepts you have learned this semester. You will build a tool capable of scrapping information from the web and storing it in a database created and maintained by your program:

You must use:

The WWW API to search the web
A Tkinter-based GUI or the Django framework to build a website (I suggest you host it on GibHub)
sqlite3 to build the database
Below you will find the details for my suggested project. If you have an idea of something else you would like to do instead, you are welcome to submit a proposal. Just make sure I approve it before you start.

 

Suggested Project
Project GutenbergLinks to an external site. is an online library of free eBooks. It has over 70,000 fee ebooks in different formats, including plain text.

Create an application capable of searching content of ebooks found in the Project Gutenberg library and save key information locally in a database created and maintained by your program. In general terms, the tool should be able to:

Given a book title, search a local database maintained by your program for the the title and retrieve the ten most frequent words in that book.
Make sure to filter words that don't add meaning to a text, such as articles, prepositions and the like. Examples of words that appear frequently and should not be considered: I, you, he, she, at, in, or, and
If the title can't be found in your local database, search the title in the Project Gutenberg and generate a list of the ten most frequent words.
Store this information (title along with the most frequent words) in the local database for next time the book is searched.
Regardless of whether the information is coming from the local database or was just retrieved from the Project Gutenberg's website, always show the ten most frequent words on the screen.
If the book cannot be found anywhere, simple say "Book was not found".
 

Minimum Requirements for the Project (Meets expectations)
Here are the basic requirements:

The interface must be on a webpage with the following components:
a text field to enter the title of the book for search in the local database
a button to search the title in the local database
when clicked, it should look for the title and display the ten most frequent words in the book along with their frequency
a text field to enter the url of the book in the Project Gutenberg library
ex: https://www.gutenberg.org/cache/epub/37106/pg37106.txtLinks to an external site. is the url for the book Little Women
a button to search the url in the Project Gutenberg website and update the local database with:
the book title and the ten most frequent words for that title
for each word, store their frequency
A place to display the list of words with their corresponding frequencies
Use exception handling constructs (try/except) to take care of errors
Document each method or function using docstrings
Add a header comment at the beginning of each file with a description of the program, your name and date
Beyond Minimum Requirements (Exceeds Expectations)
Interface is beyond the basics requirements
Added features
Submission:
The GitHub link of the repository containing your project.
Presentation:
It will be submitted as a separate discussion assignment.
The deadline for the project, including presentation submission is Friday of week 17, which is December 5th.
The following week you will watch your classmate's presentations and give feedback by the final exam date.
Practice, practice, practice!
Presentation is an important professional skill.
You will record a 5 to 7-minute presentation to show that your project works and explain how you implemented it. Practice is essential so you can convey your message in short amount of time! Less than 5 minutes is provably too short. And I won't watch past 7 minutes.
Your goal is to show how your application works and also show me you thoroughly understand the implementation.