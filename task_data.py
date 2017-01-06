import pyexcel
import pyexcel_xls
from pyexcel._compact import OrderedDict

if __name__ == '__main__':
    example_dict = {"Description": ["working on taskbuddy"],
                    "Start time": ["14:00"],
                    "End Time" : ["14:45"],
                    "Time spent": ["0h 45m 0s"],
                    "Notes": ["Finished the alpha version of taskbuddy!"]}
    sheet = pyexcel.get_sheet(adict=example_dict)
    sheet.save_as("output.csv")
    print("running")

    # data = pyexcel_xls.read_data("Thu_Jan_5_2017.xls", file_type='.xls')
    # print(data)
    # pyexcel_xls.
    # my_dict = pyexcel_xls.get_dict(file_name="Thu_Jan_5_2017.xls",
    #                            name_columns_by_row=0)
    # isinstance(my_dict, OrderedDict)
    # for key, values in my_dict.items():
    #     print({str(key): values})
