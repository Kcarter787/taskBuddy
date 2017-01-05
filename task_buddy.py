import time

FILE_FORMAT = ".xls"

class task_entry():
    def __init__(self, description):
        self.description = description
        self.note = None
        self._is_complete = False

    def mark_start_time(self):
        self.time_started, self.time_started_str, self.time_started_abs = \
            time.localtime(), time.ctime(), time.time()

    def mark_end_time(self):
        self.time_finished, self.time_finished_str, self.time_finished_abs = \
            time.localtime(), time.ctime(), time.time()

    @property
    def time_spent(self):
        seconds = self.time_finished_abs - self.time_started_abs
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "{0:}hr {1:}m {2:}s".format(int(h), int(m), int(s))

    def get_note(self):
        return self.note

    def set_note(self, note):
        self.note = note

    def get_clock_start(self):
        return self.time_started_str.split(" ")[-2]

    def get_clock_finish(self):
        return self.time_finished_str.split(" ")[-2]

    def get_date(self):
        parts = self.time_started_str.split(" ")
        date = ""
        for part in parts:
            if part and ":" not in part:
                date += part + "_"
        return date[:-1]  # Don't include trailing '_'

    # TODO: - Implement this!
    def get_american_clock_start(self):
        time = self.time_started_str.split(" ")[-2]
        h = int(time[:3])
        # Convert to american time
        ampm = "AM"
        if h >= 12:
            h -= 12
            ampm = "PM"
        if h == 0:
            hour = 12
        if h >= 12:
            time = "{}:".format(h)

    def all_data_as_csv(self):
        data = "{}, {}, {}, {}, {}\n".format(self.description,
                                       self.get_clock_start(),
                         self.get_clock_finish(), self.time_spent, self.note)
        return data

    def report_all_data(self):
        print("Details for task: '{}':\nStarted at {}\nFinished at" \
                      "at {}\nTime spent: {}\nNotes: {}\n".format(
            self.description,  self.get_clock_start(), self.get_clock_finish(),
            self.time_spent, self.note))


# TODO: - Clean up this function by breaking it up
def run_task_buddy():
    task_desc = input("What are you starting now?\n")
    task = task_entry(task_desc)
    task.mark_start_time()
    print("\nOk! Starting {} at {}! Let me know when "
                    "you’re (d)one!".format(task.description,
                                            task.get_clock_start()))
    res = ""
    while res != "d":
        res = input()
        if res != "d":
            print("Enter d if you're (d)one!")
        else:
            confirm = input("\nAre you sure you are done with '{}'? ("
                            "y/n)\n".format(
                task.description))
            if confirm == 'y':
                task.mark_end_time()
            else:
                print("\nEnter d if you're (d)one!")
                res = ""

    print("\nYou spent {} on your task '{}'".format(task.time_spent,
                                                   task.description))

    y_n = input("Would you like to add a comment to this task? (y/n)\n")
    if y_n == "y":
        note = input("\nWrite your notes below:\n")
        task.set_note(note)
        print("\nNote successfully added!")
    else:
        print("\nOk, no comments were added")

    task.report_all_data()
    file_name = "{}{}".format(task.get_date(), FILE_FORMAT)
    set_up_if_needed(file_name)
    write_results(task, file_name)


def write_results(done_task,file_name):

    with open(file_name, mode="a") as f:
        f.write(done_task.all_data_as_csv())
        prompt_restart()
        print("I Appended your data to {}".format(file_name))

def set_up_if_needed(file_name):
    try:
        with open(file_name, mode="r") as _:
            print("Found existing file")
            pass
    except FileNotFoundError:
        with open(file_name, mode="a") as f:
            print("Making new file")
            f.write("Description, Start time, End Time, Time Spent,"
                            " Notes\n")


def prompt_restart():
    res = input("\nWould you like to continue documenting your time? (y/n)\n")
    if res == "y":
        run_task_buddy()
    else:
        print("\nEnding program. Start me up again when you want to document "
              "your time!\n")

def main():
    print("\nWelcome to taskJournal, I suggest you log everything you do "
          "during your work day including breaks.\n")
    run_task_buddy()

if __name__ == '__main__':
    main()
