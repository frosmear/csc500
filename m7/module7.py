# CSC500 Module 7 

# CSC500 Course Information System
#
# This program uses separate dictionaries to store course information.
# The course number is used as the key so the program can retrieve
# the room, instructor, and meeting time for a course.
#

from datetime import datetime

# If I were doing this for a government training office this would almost
# certainly being in an Excel spreadsheet I'd dump to CSV and parse

course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Meeting times were not provided in the assignment, so I created
# sample Fall 2026 meeting dates/times for the demonstration.

course_meeting_times = {
    "CSC101": datetime(2026, 9, 8, 9, 0),
    "CSC102": datetime(2026, 9, 9, 11, 0),
    "CSC103": datetime(2026, 10, 6, 13, 30),
    "NET110": datetime(2026, 10, 8, 18, 0),
    "COM241": datetime(2026, 11, 3, 14, 0)
}


# Get a course number from the user and clean up the input.
def get_course_number():
    while True:
        course_number = input(
            "Enter course number (example: CSC101): "
        ).strip().upper()

        if course_number == "":
            print("Course number cannot be blank.")
            continue

        return course_number


# Check whether the course exists in all three dictionaries.
def course_exists(course_number):
    if course_number not in course_rooms:
        return False

    if course_number not in course_instructors:
        return False

    if course_number not in course_meeting_times:
        return False

    return True


# Display all information for a course.
def display_course(course_number):
    meeting_time = course_meeting_times[course_number]

    print("\nCourse Information")
    print("------------------")
    print(f"Course Number: {course_number}")
    print(f"Room Number:   {course_rooms[course_number]}")
    print(f"Instructor:    {course_instructors[course_number]}")
    print(
        f"Meeting Time:  "
        f"{meeting_time.strftime('%B %d, %Y at %I:%M %p')}"
    )


# Main program
def main():
    print("CSC500 Course Information System")

    course_number = get_course_number()

    if not course_exists(course_number):
        print(
            f"Sorry, course {course_number} was not found. "
            "Please check the course number and try again."
        )
        return

    display_course(course_number)


if __name__ == "__main__":
    main()


