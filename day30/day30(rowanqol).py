# Yeah, I made my own lib
import rowanqol

integer = rowanqol.int_input("Input an integer!", error_msg="Input an INTEGER.")
floaty = rowanqol.float_input("Input a float!", error_msg="Input a FLOAT.")
print(f"You said '{integer}' and '{floaty}'.")