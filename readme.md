# Day Planner
---
A simple plugin to generate a day planner from a timetable and several spreadsheets.

## Setup
---
To set up this plugin, there are 3 steps:
1. Clone this repo.
    If you don't use git, click the green `<> Code` button in the top right and download the zip folder. Extract it wherever you'd like.

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
