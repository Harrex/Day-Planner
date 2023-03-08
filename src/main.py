import pandas
import mdutils
import datetime
import json

import os, sys

def main():
    lesson_indexes = json.load(open("lesson_indexes.json"))
    column_number = lesson_indexes["Column Number"]
    while True:
        if lesson_indexes["Ask for week numbers"]: # Read the JSON file - If this value is true, ask for the week number, otherwise just run
            if create_timetable(input("Current Week (A/B): "), lesson_indexes, column_number):
                input("Success! Press enter to continue.")
                break
            else:
                input("Failed to create timetable - Did you type the week correctly? \n Press enter to continue.")
                break
        else:
            if create_timetable("A", lesson_indexes, column_number):
                input("Success! Press enter to continue.")
                break
            else:
                input("Failed to create timetable - Have you set up the program correctly? Check the github page or the readme for instructions. \n Press enter to continue.")
                break

def create_timetable(current_week:str, lesson_indexes, column_number):
    try:
        timetable = json.load(open(current_week + ".json"))
    except:
        return False

    day = datetime.date.today().strftime("%A")
    print(day)
    if lessons := timetable[day]:
        today_lesson_plans = []
        sheet = pandas.read_excel("Lesson Plans/" + lesson + ".xlsx", header=None)

        for lesson in lessons:
            current_lesson = int(lesson_indexes[lesson])
            json.dump(lesson_indexes, open(
                "lesson_indexes.json", 'w'), indent=4)
            plan = sheet.iloc[int(current_lesson)][column_number]
            today_lesson_plans.append((lesson, current_lesson, plan))
            lesson_indexes[lesson] = current_lesson + 1
    else:
        today_lesson_plans = []

# ---------------------------------------------------------------------------- #
# Creating MD file. If you want to mess with your template, here is the place. #
# ---------------------------------------------------------------------------- #
    print(today_lesson_plans)
    final_file = mdutils.MdUtils(file_name = ("../Day Planner/" + str(datetime.date.today()) + ".md"), title=f"{day}, Week {current_week}, {str(datetime.date.today())}")
    period = 0
    if today_lesson_plans:
        for lesson_plan in today_lesson_plans:
            period += 1
            final_file.new_header(
                level=1, title=f"Period {period} - {lesson_plan[0]}, lesson #{lesson_plan[1]}")
            if type(lesson_plan[2]) == str:
                final_file.new_paragraph(lesson_plan[2])
            else:
                final_file.new_paragraph("No Lesson Plan!")
            final_file.new_line()
            final_file.new_line("---")
    else:
        final_file.new_header(
            level=1, title="Either it's the weekend or I'm broken...")

    final_file.create_md_file()
    return True




if __name__ == "__main__":
    main()