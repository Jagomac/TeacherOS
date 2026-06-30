import os

commands = {
    "ls": {
        "meaning": "Lists files and directories",
        "options": {
            "-l": "Long listing format (permissions, size, date)",
            "-a": "Include hidden files"
        },
        "english": "Show all files in this directory, including hidden ones, with details."
    },

    "pwd": {
        "meaning": "Print Working Directory",
        "options": {},
        "english": "Show me where I am in the system."
    },

    "mkdir": {
        "meaning": "Make directory",
        "options": {},
        "english": "Create a new folder."
    },

    "cd": {
        "meaning": "Change directory",
        "options": {},
        "english": "Move into a different folder."
    },

    "rm": {
        "meaning": "Remove files or directories",
        "options": {
            "-r": "Remove directories recursively",
            "-f": "Force removal (no confirmation)"
        },
        "english": "Delete files or folders (be careful!)"
    }
}


def explain(command_input):
    parts = command_input.split()

    if not parts:
        return

    cmd = parts[0]

    if cmd in commands:
        info = commands[cmd]

        print("\n==============================")
        print("📖 TEACHEROS LESSON")
        print("==============================")

        print(f"\n🖥 Command: {cmd}")
        print(f"📌 Meaning: {info['meaning']}")

        if info["options"]:
            print("\n⚙ Options:")
            for opt, desc in info["options"].items():
                print(f"   {opt} -> {desc}")

        print("\n🧠 Equivalent English:")
        print(f"   {info['english']}")

        if cmd == "rm":
            print("\n⚠️ Risk Level: HIGH (Deletes files!)")

    else:
        print("\n⚠️ Unknown command (no lesson available yet)")


def run():
    while True:
        user_input = input("\n$ ")

        if user_input.strip() == "":
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        explain(user_input)

        choice = input("\n[Y] Yes  [N] No  [M] More > ").lower()

        if choice == "y":

            if user_input.startswith("rm"):
                print("\n⚠️ WARNING: This command deletes files.")
                confirm = input("Type YES to confirm: ")

                if confirm == "YES":
                    os.system(user_input)
                else:
                    print("Command canceled.")
            else:
                os.system(user_input)

        elif choice == "m":
            print("\n💡 Examples:")
            print("ls")
            print("ls -l")
            print("pwd")
            print("mkdir test_folder")

        else:
            print("Command canceled.")


if __name__ == "__main__":
    run()
