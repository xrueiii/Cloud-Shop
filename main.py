from app.database.db import init_db
from app.presentation.commandController import commandLoop

if __name__ == "__main__":
    init_db()
    commandLoop()
