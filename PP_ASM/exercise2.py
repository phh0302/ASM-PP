"""Exercise 2: Manage student data using pandas."""

import pandas as pd

CSV_FILE = "students.csv"


def create_students():
    """Create a DataFrame with at least 5 students."""
    data = {
        "id": [1, 2, 3, 4, 5, 6],
        "name": ["Nguyen Van A", "Tran Thi B", "Le Van C",
                 "Pham Thi D", "Hoang Van E", "Do Thi F"],
        "age": [20, 21, 19, 22, 20, 21],
        "score": [8.5, 4.0, 9.0, 6.5, 3.5, 8.0],
    }
    return pd.DataFrame(data)


def save_to_csv(df, file_path):
    """Save the DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)
    print(f"Saved {len(df)} students to {file_path}")


def read_from_csv(file_path):
    """Read the CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def main():
    # 1. Create DataFrame and save to CSV
    students = create_students()
    save_to_csv(students, CSV_FILE)

    # 2. Read the CSV file
    df = read_from_csv(CSV_FILE)

    print("\n===== ALL STUDENTS =====")
    print(df.to_string(index=False))

    print("\n===== STUDENTS WITH SCORE >= 8 =====")
    print(df[df["score"] >= 8].to_string(index=False))

    # 3. Average score
    print(f"\nAverage score: {df['score'].mean():.2f}")

    # 4. Add new column: result = "Pass" if score >= 5 else "Fail"
    df["result"] = df["score"].apply(lambda s: "Pass" if s >= 5 else "Fail")
    print("\n===== STUDENTS WITH RESULT =====")
    print(df.to_string(index=False))

    # Save the updated data (with result column)
    save_to_csv(df, CSV_FILE)


if __name__ == "__main__":
    main()
