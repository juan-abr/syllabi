# syllabi

## Description
A Django web app that organizes the requirements of a martial arts school by
rank and category, and then generates webpages that displays those requirements
as an individual syllabus for each of the school's ranks.

## Installation
If you already have a Django project up and running, all you need is to:
1. add the repo to your project folder,
2. type "'syllabi'" into Installed Apps, and
3. include the syllabi urls to the main project folder's url patterns.

If you need more information on how to start a Django project, the Django polls tutorial in the documentation for Django is a fantastic place to start.

## How it works
From the admin page of your project, you should have the option to add:
1. Ranks - A level or degree that a martial arts student can achieve. Can be added before or after you add Categories to the database.
2. Categories - The under which requirements are defined. Categories may include Hand Techniques or martial arts Forms. Can be added before or after you add Ranks to the database.
3. Requirements - Individual techniques or combinations that a student must complete in order to rank up. This should be the last of the three that you add to your database.

Add these to your web app, select the Rank and Category the requirement belongs to, and it will be added to the syllabus associated with that rank. Media and additional eligibility requirements can also be added to a rank or requirement respectively.

For more information, please do not hesitate to contact me.
