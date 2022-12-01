# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Simple calculator of body mass index (BMI)
#              by demonstrating use of pickling and exception
#              Handling in Python
# ChangeLog (Who,When,What):
# TTadesse,11.28.2022, Created script
# TTadesse,11.29.2022, Added Exception Handling
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #

thefile = 'bmi.dat'
list_BMI = []
menu_choice = ""

# Processing  --------------------------------------------------------------- #
class Pickling:
    """  Performs Processing tasks """

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """ Writes data from a list of rows to a file in binary mode

        :param file_name: (string) name of file:
        :param list_of_data: (list) data in dictionary to be saved in file:
        :return: nothing
        """
        file = open(file_name, 'ab')
        pickle.dump(list_of_data, file)
        file.close()


    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a binary file into rows of lists

        :param file_name: (string) with name of file:
        :return: lists of data
        """
        file = open(file_name, 'rb')
        data = pickle.load(file)
        file.close()
        return data

# Presentation (Input/Output)  ---------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print("\n Let's Calculate Your Body Mass Index (BMI) \n")
        print('''
        1) Calculate in Metric Unit
        2) Calculate in Imperial Unit
        3) Display BMI and Explanation
        4) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string of a digit
        """
        menu_choice = str(input("What would you like to perform? Please enter [1 to 4] "))
        print()
        return menu_choice

    @staticmethod
    def input_weight_height_in_metric():
        """  Gets weight and height of a user to calculate BMI in metric unit

        :return: (float, float) weight and height
        """
        weight = float(input("What is your weight in kG? "))
        height = float(input("What is your height in meters? "))

        return weight, height

    @staticmethod
    def input_weight_height_in_imperial():
        """  Gets weight and height of a user to calculate BMI in imperial unit

        :return: (float, float) weight and height
        """

        weight = float(input("What is your weight in pounds? "))
        height = float(input("What is your height in inches? "))

        return weight, height

    @staticmethod
    def output_description_BMI(BMI):
        """ Outputs descriptions of BMI ranges that fits the user BMI

        :return:nothing
        """
        if BMI <= 18.5:
            print("Your BMI falls within the underweight range. \n")
        elif BMI >= 24.9:
            print("Your BMI falls within the overweight range. \n")
        else:
            print("Your BMI falls within healthy weight range. \n")


# Main Body of Script  --------------------------------------------------------- #


while (True):
    # Step 1 Display a menu of choices to the user and ask for a menu of choice
    IO.output_menu_options()  # Shows menu
    menu_choice = IO.input_menu_choice()  # Get menu option

    # Step 2 - Process user's menu choice
    if menu_choice.strip() == '1':  # use metric method to take data from user
        try:
            weight, height = IO.input_weight_height_in_metric()
            BMI = weight/(height*height)
            list_BMI = [weight, height, BMI]
            Pickling.save_data_to_file(file_name=thefile, list_of_data=list_BMI)
        except ValueError as v:
            print("Your weight and height should only be a number \n")
            print("Built-In Python error info:")
            print(v.__doc__, type(v), sep='\n')
        except ZeroDivisionError as z:
            print("your height cannot be zero \n")
            print("Built-In Python error info:")
            print(z.__doc__, type(z), sep='\n')
        except FileNotFoundError as f:
            print("Binary data must exist before running this script")
            print("Built-In Python error info:")
            print(f.__doc__, type(f), sep='\n')
        try:
            if height >= 2.8:
                raise Exception("Height should be in meters" )
        except Exception as e:
            print("Are you taller than the tallest man in the world?")
            print("try again")
            print("Built-In Python error info:")
            print(e.__doc__, type(e), sep='\n')

            continue  # to show the menu

    if menu_choice.strip() == '2':  # use imperial method to take data from user
        try:
            weight, height = IO.input_weight_height_in_imperial()
            BMI = weight/(height*height)  # calculate the BMI
            list_BMI = [weight, height, BMI]
            Pickling.save_data_to_file(file_name=thefile, list_of_data=list_BMI)

        except ValueError as v:
            print("Your weight and height should only be a number \n")
            print("Built-In Python error info:")
            print(v.__doc__, type(v), sep='\n')
        except ZeroDivisionError as z:
            print("your height cannot be zero \n")
            print("Built-In Python error info:")
            print(z.__doc__, type(z), sep='\n')

        except FileNotFoundError as f:
            print("Binary data must exist before running this script")
            print("Built-In Python error info:")
            print(f.__doc__, type(f), sep='\n')
        try:
            if height <= 10:
                raise Exception("Enter height in units of inches, not feet")
        except Exception as e:
            print("Did you mean to put your height in inches, not feet?")
            print("Built-In Python error info:")
            print(e.__doc__, type(e), sep='\n')
            continue  # to show the menu
    elif menu_choice == '3':  # Explains what the BMI mean
        list_BMI = Pickling.read_data_from_file(file_name=thefile)  # read file data
        current_BMI = round(float(list_BMI[2]), 1)
        print("Your Current BMI is " + str(current_BMI))
        IO.output_description_BMI(BMI=current_BMI)
        continue  # to show the menu

    elif menu_choice == '4':  # Exit Program
        print("Thank you! Check the CDC Website for More Information!")
        break  # by exiting loop
