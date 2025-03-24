import re
from marketplace import Marketplace
from database import init_db

init_db()

def main():
    while True:
        try:
            command = input("# ").strip()  # 顯示 prompt
            if not command:
                continue

            args = command.split(" ", 1)
            cmd = args[0]

            if cmd == "REGISTER":
                print(Marketplace.register_user(args[1]))

            elif cmd == "CREATE_LISTING":
                # 用 regex 解析參數：username + 3 個 '...' + price + '...'
                match = re.match(r"(\S+)\s+'(.+)'\s+'(.+)'\s+(\d+)\s+'(.+)'", args[1])
                if not match:
                    print("Error - invalid CREATE_LISTING format")
                    continue

                username = match.group(1)
                title = match.group(2)
                description = match.group(3)
                price = int(match.group(4))
                category = match.group(5)

                print(Marketplace.create_listing(username, title, description, price, category))

            elif cmd == "DELETE_LISTING":
                username, listing_id = args[1].split()
                print(Marketplace.delete_listing(username, int(listing_id)))

            elif cmd == "GET_LISTING":
                username, listing_id = args[1].split()
                print(Marketplace.get_listing(username, int(listing_id)))

            elif cmd == "GET_CATEGORY":
                match = re.match(r"(\S+)\s+'(.+)'", args[1])
                if not match:
                    print("Error - invalid GET_CATEGORY format")
                    continue
                username = match.group(1)
                category = match.group(2)
                print(Marketplace.get_category(username, category))

            elif cmd == "GET_TOP_CATEGORY":
                print(Marketplace.get_top_category(args[1]))

        except EOFError:
            break
        except Exception as e:
            print(f"Error - {str(e)}")

if __name__ == "__main__":
    main()