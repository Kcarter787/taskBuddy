import time
import bot_strings as bs

FILE_NAME = "task_log"
FILE_FORMAT = ".csv"


class taskEntry():
    def __init__(self, description, time_estimate):
        self.description = description
        self.time_estimate = time_estimate
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
                date += part + " "
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
        data = "{}, {}, {}hr {}min, {}, {}, {}, {}\n" \
            .format(self.get_date(),
                    self.description,
                    self.time_estimate[0],
                    self.time_estimate[1],
                    self.get_clock_start(),
                    self.get_clock_finish(),
                    self.time_spent,
                    self.note)
        return data

    def report_all_data(self):
        print("Details for task: '{}':\nStarted at {}\nFinished at" \
              "at {}\nTime spent: {}\nNotes: {}\n".format(
            self.description, self.get_clock_start(), self.get_clock_finish(),
            self.time_spent, self.note))

def get_time_estimate(first_attempt=True):
    if first_attempt:
        estimate = input(bs.estimate_question())
    else:
        estimate = input(bs.estimate_format_error_msg())
    parts = estimate.split(',')
    if len(parts) == 2:
        hr, min = parts[0].strip(), parts[1].strip()
        if hr.isnumeric() and min.isnumeric():
            return hr, min
    else:
        get_time_estimate(first_attempt=False)

def build_task_entry():
    task_desc = input(bs.taskname_question())
    time_estimate = get_time_estimate()
    task = taskEntry(task_desc, time_estimate)
    task.mark_start_time()
    return task


def wait_until_done(task):
    """
    :type task: taskEntry
    """
    res = ""
    while res != "d":
        res = input()
        if res != "d":
            print(bs.done_requirement_reminder())
        else:
            confirm = input(bs.done_confirmation(task))
            if confirm == 'y':
                task.mark_end_time()
            else:
                print("\n{}".format(bs.done_requirement_reminder()))
                res = ""


#TODO: - This could still be made cleaner
def run_task_buddy():
    task = build_task_entry()
    print(bs.response_to_taskname(task))
    wait_until_done(task)
    print(bs.result_description(task))
    y_n = input(bs.add_comment_question())
    if y_n == "y":
        note = input(bs.note_prompt())
        task.set_note(note)
        print(bs.note_success_msg())
    else:
        print(bs.note_denied_msg())
    task.report_all_data()
    file_name = "{}{}".format(FILE_NAME, FILE_FORMAT)
    set_up_if_needed(file_name)
    write_results(task, file_name)


def write_results(done_task, file_name):
    with open(file_name, mode="a") as f:
        f.write(done_task.all_data_as_csv())
        prompt_restart()
        print("I Appended your data to {}".format(file_name))


# TODO: - Move the rest of the strings to separate file
def set_up_if_needed(file_name):
    try:
        with open(file_name, mode="r") as _:
            print("Found existing file")
            pass
    except FileNotFoundError:
        with open(file_name, mode="a") as f:
            print("Making new file")
            f.write(bs.log_headers())


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
