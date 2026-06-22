from wat import wat
password = "super_secret_password"
name = "Byte"
user_name = "player1"
player_name = "Hero"
is_logged_in = True
is_active = True
has_access = False
error_flag = False
debug_mode = True
temp_value = 42
current_index = 0
max_value = 100
min_value = 0
data_list = [1, 2, 3, 4]
data_dict = {"a": 1, "b": 2}
response = "OK"
result = 3.14
output = "success"
input_data = "test_input"
file_path = "save/data.json"
save_file = True
config = {"volume": 80, "brightness": 60}
settings = {"difficulty": "normal"}
session_id = "sess_9f3k2"
token = "abc123xyz"
auth_key = "key_9876"
password_hash = "hashed_value"
retry_count = 3
timeout = 30
buffer = ""
cache = {}
queue = [1, 2, 3]
stack = []
node = "root"
tree_root = {"left": None, "right": None}
left_child = None
right_child = None
is_valid = True
is_ready = False
has_error = False
status_code = 200
message = "All systems go"
event = "start"
event_queue = ["init", "load", "run"]
last_update = "2026-06-22"
timestamp = 1719072000
delta_time = 0.016
position_x = 100
position_y = 250
velocity = 5
acceleration = 0.2
direction = "north"
health = 100
mana = 75
score = 999
level = 5
experience = 1234
while True:
    prompt = input("guess some variable names. oh and type q to quit. ").strip().lower()
    if prompt == "q":
        break
    try:
        variable = globals()[prompt]
        wat / variable
    except KeyError:
        print("no such variable")
    except Exception as e:
        print(e)