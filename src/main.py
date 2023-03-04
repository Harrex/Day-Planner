import pandas
import mdutils
import datetime
import json

import os, sys


column_number = 1


lesson_indexes_file = open("lesson_indexes.json")
lesson_indexes = json.load(lesson_indexes_file)


# Don't look at this bit it's embarrasing
def create_timetable(current_week:str):
    try:
        timetable = json.load(open(current_week + ".json"))
    except:
        return False

    day = datetime.date.today().strftime("%A")
    print(day)
    if lessons := timetable[day]:
        today_lesson_plans = []

        for lesson in lessons:
            sheet = pandas.read_excel("Lesson Plans/" + lesson + ".xlsx", header=None)
            current_lesson = int(lesson_indexes[lesson])
            lesson_indexes_file.seek(0)
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


while True:
    if lesson_indexes["Ask for week numbers"]:
        if create_timetable(input("Current Week (A/B): ")):
            input("Success! Press any key to continue.")
            break
        else:
            print("Failed to create timetable - Did you type the week correctly?")
    else:
        create_timetable("A")