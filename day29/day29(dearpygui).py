import dearpygui.dearpygui as dpg
import pandas as pd

dpg.create_context()

try:
    data = pd.read_excel("data.xlsx")
except FileNotFoundError:
    raise FileNotFoundError("Can't find the data file.") # Gives explanation of why we are getting the error. May be useful for some.
data_dict = data.to_dict(orient="records")
print(data_dict)
def submit():
    global data_dict, data
    username = dpg.get_value("username")
    level = dpg.get_value("level")
    next_id = int(data.iloc[-1, 0]) + 1 if not data.empty else 0
    new_row = pd.DataFrame([{"id": next_id, "name": username, "level": level}])
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_excel("data.xlsx", index=False)
    dpg.set_value("status_message", "Submitted successfully! Please close this window.")
with dpg.window(label="Record stats", width=800, height=600):
    dpg.add_text("Username")
    dpg.add_input_text(tag="username", label="Username")
    dpg.add_text("Level")
    dpg.add_input_text(tag="level", label="Level")
    dpg.add_button(label="Submit", callback=submit)
    dpg.add_text("", tag="status_message")

dpg.create_viewport(title="Day 29 - A Form", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()