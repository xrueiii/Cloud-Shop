# CloudShop

This is a command-line marketplace application built in Python, following a clean layered architecture. It supports registering users, creating and managing listings, querying by category, and fetching the top categories in the marketplace.

---

## 🚀 Features

- Register new users
- Create, retrieve, and delete listings
- List all listings under a category (sorted by newest first)
- Show the most popular category (based on number of listings)
- Case-insensitive username and category handling
- CLI-based interface with `#` prompt
- Uses SQLite for persistent storage
- Cleanly separated into:
  - **presentation** layer (CLI parsing)
  - **service** layer (business logic)
  - **persistence** layer (SQLite interaction)
  - **model** layer (data structure)
  - **database** layer (DB setup/connection)

---

## 🛠 Environment

- **Language**: Python 3.11.7
- **Database**: SQLite 3 
- **System**:  macOS Sequoia 15.3.1

---

## 📦 Folder Structure

```
cloudshop/
|
├── app/ 
│ ├── presentation/ ← CLI controller 
│ ├── service/ ← Business logic 
│ ├── persistence/ ← SQLite DB access 
│ ├── model/ ← Data models 
│ └── database/ ← DB init and connection
|
├── run.sh ← Run the program 
├── build.sh ← Give permissions to shell scripts 
├── Makefile ← Easy build/run/clean commands 
├── main.py ← Entry point 
├── README.md ← You're reading it!
```

---

## 🔧 How to Build & Run

### 1. Clone or unzip project
```bash
git clone <repo> cloudshop
cd cloudshop
```

### 2. Download SQLite
```bash
sudo apt install python3 sqlite3 -y  # Ubuntu
brew install python3 sqlite3         # MacOS
```

### 3. Make scripts executable
```bash
make build
```

### 4. Run the CLI
```bash
make run
```

Then, You'll now see this prompt:
```bash
#
```

🥳 You can start entering commands like:
```bash
# REGISTER user1
# CREATE_LISTING user1 'Phone model 8' 'Black color' 1000 'Electronics'
```
---

## 📘 Supported Commands

Below is a list of all supported CLI commands:

| Command Format                                                                 | Description                                       |
|--------------------------------------------------------------------------------|---------------------------------------------------|
| `REGISTER <username>`                                                          | Registers a new user.                            |
| `CREATE_LISTING <username> <title> <description> <price> <category>`    | Creates a new listing under the specified user.  |
| `DELETE_LISTING <username> <listing_id>`                                      | Deletes the specified listing.                   |
| `GET_LISTING <username> <listing_id>`                                         | Retrieves full details of a listing.             |
| `GET_CATEGORY <username> <category>`                                        | Retrieves all listings under a category, sorted by most recent.                                           
| `GET_TOP_CATEGORY <username>`                                                 | Returns the most popular category (by listing count). |
                                                                               

---

## 🧪 Testing Tips

You can pipe test input into the program:

```bash
make run < test_input.txt
```

---

## 🧹 Useful Make Commands

| Command       | Description                    |
|---------------|--------------------------------|
| `make build`  | Grant permissions to scripts   |
| `make run`    | Launch CLI program             |
| `make clean`  | Delete the SQLite database     |

---

## 📄 Notes

- All error messages are printed to **STDOUT** (not STDERR).
- `listing_id` starts from **100001**, increasing sequentially.
- Input values like `<title>`, `<description>`, `<category>` must be wrapped in **single quotes `'...'`** to avoid parsing errors.
- `GET_TOP_CATEGORY` returns **multiple categories alphabetically** if there’s a tie.
- All commands are **case-insensitive** where required (e.g., `username`, `category`).
- Assumes all numeric inputs are valid **integers** (e.g., no floating-point price).

---

## 👨‍💻 Maintainer

**Sophie Ku @ NTU IM**  
Email: b11705043@g.ntu.edu.tw
