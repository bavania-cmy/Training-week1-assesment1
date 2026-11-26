import csv
import json
import os
from pathlib import Path
import requests
from dotenv import load_dotenv


def process_csv_files(data_dir):
    employees_csv = data_dir / "employees.csv"
    employees_json = data_dir / "employees.json"
    high_earners_csv = data_dir / "high_earners.csv"

    # 1. Read employees.csv with csv.DictReader
    employees = []
    with open(employees_csv, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            row["id"] = int(row["id"])
            row["salary"] = int(float(row["salary"]))
            employees.append(row)

    # 2. Write all records to employees.json
    with open(employees_json, mode="w", encoding="utf-8") as jf:
        json.dump(employees, jf, indent=4)

    # 3. Filter salary > 50000 and write to high_earners.csv
    high_earners = [emp for emp in employees if emp["salary"] > 50000]
    with open(high_earners_csv, mode="w", encoding="utf-8", newline="") as hf:
        writer = csv.DictWriter(hf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(high_earners)

    print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")


def fetch_and_save_users(base_dir, data_dir):
    # 4. Load API_KEY from .env
    load_dotenv(base_dir / ".env")
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise EnvironmentError("API_KEY missing in .env file.")

    base_url = "https://typicode.com"
    headers = {"Authorization": f"Bearer {api_key}"}
    users_json = data_dir / "users.json"

    # 5. GET /users with timeout=5 and exception handling
    try:
        response = requests.get(f"{base_url}/users", headers=headers, timeout=5)
        response.raise_for_status()
        users_data = response.json()

        # Print id, name, and email of first 3 users
        for user in users_data[:3]:
            print(f"{user.get('id')} - {user.get('name')} - {user.get('email')}")

        # 6. Safely parse nested JSON fields with .get() and write to users.json
        parsed_users = []
        for user in users_data:
            address = user.get("address", {})
            company = user.get("company", {})
            parsed_users.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "city": address.get("city", "Unknown"),
                "zipcode": address.get("zipcode", "N/A"),
                "company_name": company.get("name", "Independent"),
            })

        with open(users_json, mode="w", encoding="utf-8") as uf:
            json.dump(parsed_users, uf, indent=4)

    except requests.exceptions.Timeout:
        print("Request timed out while fetching /users.")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred while reaching the API.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")

    # 7. Handle 404 on /users/9999
    try:
        not_found_res = requests.get(f"{base_url}/users/9999", headers=headers, timeout=5)
        if not_found_res.status_code == 404:
            print("/users/9999 -> 404 Not found")
        else:
            not_found_res.raise_for_status()
    except requests.exceptions.Timeout:
        print("/users/9999 -> Request timed out")
    except requests.exceptions.ConnectionError:
        print("/users/9999 -> Connection error-404 not found")


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    data_folder = root_dir / "data"
    data_folder.mkdir(exist_ok=True)

    process_csv_files(data_folder)
    fetch_and_save_users(root_dir, data_folder)