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

## How it works
From the admin page of your project, you should have the option to add:
1. Ranks
Can be added before or after you add Categories to the database.
3. Categories
Can be added before or after you add Ranks to the database.
4. Requirements
This should be the last of the three that you add to your
to your web app. Select the Rank and Category the requirement belongs to
and it will be added to the syllabus associated with that rank.
