from gooey import Gooey, GooeyParser
import pandas as pd
data = pd.read_csv("data.csv")
@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument("name", help="Enter your name")
    parser.add_argument("age", help="Enter your age")
    parser.add_argument("email", help="Enter your email")
    args = parser.parse_args()
    new_data = pd.DataFrame(
        [[int(data.iloc[-1, 0]) + 1, args.name, args.age, args.email]],
        columns=["ID", "Name", "Age", "Email"]
    )
    new_data.to_csv("data.csv", mode="a", index=False, header=False)
    print(f"Hello, {args.name}!")
    print()
if __name__ == "__main__":
    main()