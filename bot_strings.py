def ask_for_taskname():
    return "What are you starting now?\n"


def response_to_taskname(task):
    return "\nOk! Starting {} at {}! Let me know when you’re (" \
           "d)one!".format(task.description, task.get_clock_start())
