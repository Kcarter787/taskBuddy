import task_buddy as tb

def log_headers():
    return "Date, Description, My Estimate, Start time, End Time, " \
           "Time Spent, Notes\n"

def taskname_question():
    return "What are you starting now?\n"

def estimate_question():
    return "How long do you think it will take? (hr, min) \n"

def estimate_format_error_msg():
    return "Please enter your time estimate using two numbers in the " \
           "following format: hr, min\n"

def response_to_taskname(task):
    """
    :type task: taskEntry
    """
    return "\nOk! Starting {} at {}! Let me know when you’re (" \
           "d)one!".format(task.description, task.get_clock_start())

def done_requirement_reminder():
    return "Enter d if you're (d)one!"

def done_confirmation(task):
    """
    :type task: taskEntry
    """
    return "\nAre you sure you are done with '{}'? (y/n)\n".format(
        task.description)

def result_description(task):
    """
    :type task: taskEntry
    """
    return "\nYou spent {} on your task '{}'".format(task.time_spent,
                                                     task.description)

def add_comment_question():
    return "Would you like to add a comment to this task? (y/n)\n"

def note_prompt():
    return "\nWrite your notes below:\n"

def note_success_msg():
    return "\nNote successfully added!"

def note_denied_msg():
    return "\nOk, no comments were added"