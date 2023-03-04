# Day Planner
A simple plugin to generate a day planner from a timetable and several spreadsheets.
This program is windows only. If you want to use it on something else, send me a message and I may build a version for Mac or Linux.

Example:
---
```
Friday, Week A, 2023-03-03
==========================

# Period 1 - Subject 1, lesson #1


Do a thing  
  
---
# Period 2 - Subject 2, lesson #2


Do another thing  
  
---
# Period 3 - Subject 3, lesson #3


Do a third thing  
  
---
# Period 4 - Subject 4, lesson #4


Lorem impusm  
  
---
```
This will look different depending on which editor you use. That's how it would look in notepad.
---

## Setup
---
To set up this plugin, there are 5 steps:
1. Clone this repo or download as ZIP
    If you don't use git, go to the green `<> Code` button in the top right, and download as ZIP. Extract this to a sensible location (not downloads) and go into the `Final` folder.

2. Add your spreadsheets to the `Lesson Plans` folder. 

3. Set your timetable
    To add your timetable, go to `A.json` and `B.json`. If you're schedule is weekly, not fortnightly, lucky you! You can delete `B.json`.
    Here, set your timetable for each day. Have as many classes as you'd like, but make sure you have them surrounded by a string. They should match your spreadsheet names.
    Here is an example:

```
"Monday":["Y10 Maths", "Y7 English", "Y11 Music", "Y12 History"]
```


4. Set your preferences
In the `lesson_indexes.json` file, you can set several preferences:
    1. `Ask for week numbers` - This controls whether the program will ask what week it is. If you schedule is over multiple weeks, leave this as `true`. Else, set it to `false`, and the program will simply check `A.json` for your timetable.
    2. `Column Number` - This option sets which column the program will look for your lesson plans. Whatever is in this column will be added to the day plan. Columns start from 0: A is column 0, B is 1, C is 2 etc.
    3. `Subject X` - These are your lesson numbers. Change the subject to whatever you had on the timetable (matching the spreadsheet), and set the index to whatever row you're looking up. Once again, rows start from 0, so row 1 is actually row 0 etc. Set this to whatever lesson you'll teach *next*.
    4. `Lesson Plan Path` - This is the folder that the final lesson plans will appear in. Set this to a path like the following:
```
"Lesson Plan Path": "C:/Users/[Username]/Desktop/Lesson Plans"
```
    To get the path to a folder on Windows, right click on the folder and click `Copy As Path`. You will have to replace all of the backslashes (\) with forward slashes (/) because backslashes can cause issues.


5. Run `main.exe` 
    Running this will first ask you what week it is (If you have that enabled), then generate the file with the current date, eg. `2023-03-02.md`. This file will open in any markdown viewer, such as Notepad, Obsidian, or Typora. These files won't be edited after creation, so feel free to add things to them after they've been generated.




## Data
I don't see anything of yours, and the program only reads what it needs to. If you don't trust me, you can read the code.
