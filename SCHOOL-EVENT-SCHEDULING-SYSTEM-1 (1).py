events = []
archived_events = []


while True:
    print("\n---Select Option---")
    print("[1] Admin")
    print("[2] Student")
    print("[3] Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("\n---Login!---")
        user = input("User: ")
        password = input("Pass: ")
        if user == "Admin123" and password == "Password123":
            while True:
                print("\n----- ADMIN DASHBOARD -----")
                print("[1] View Events")
                print("[2] Add Event")
                print("[3] Edit Event")
                print("[4] Archive Event")
                print("[5] Back")
                admin_choice = input("Choose: ")

                
                if admin_choice == "1":
                    if not events:
                        print("No events found.")
                    else:
                        print("\n{:<4} {:<25} {:<12} {:<40}".format("No.", "Event List", "Date", "Description"))
                        print("-" * 85)
                        for i, e in enumerate(events, 1):
                            print("{:<4} {:<25} {:<12} {:<40}".format(
                            i,
                            str(e['title']),
                            str(e['date']),
                            str(e['description'])
                            )) 

                        
                elif admin_choice == "2":
                    while True:
                        title = input("Title: ").strip()
                        if title == "":
                            print("Title cannot be empty. Please enter a valid title.")
                            continue
                        from datetime import datetime
                        while True:
                            date = input("Date (MM-DD-YYYY): ").strip()

    # Split by dash
                            parts = date.split("-")
                            if len(parts) != 3:
                                print("Invalid format. Use MM-DD-YYYY.")
                                continue

                            mm, dd, yyyy = parts

                            if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
                                print("Month, Day, and Year must be numbers.")
                                continue

                            mm = int(mm)
                            dd = int(dd)
                            yyyy = int(yyyy)

                            if mm < 1 or mm > 12:
                                print("Invalid month. Must be 1 to 12.")
                                continue
                            if dd < 1 or dd > 31:
                                print("Invalid day. Must be 1 to 31.")
                                continue
                            if yyyy < 1000 or yyyy > 9999:
                                print("Invalid year. Must be 4 digits.")
                                continue

    
                            break


                        description = input("Description: ").strip()
                        if description == "":
                            print("Description cannot be empty. Please enter a valid description.")
                            continue

                        events.append({"title": title, "date": date, "description": description})
                        print("Event Added!")
                        break


                elif admin_choice == "3":
                    if not events:
                        print("No events to edit.")
                        continue
                    else:
                        print("\nNo. | Title                 | Date        | Description")
                        print("----------------------------------------------------------")
                        for i, e in enumerate(events, 1):
                            print(f"{i:<4}| {e['title']:<25}| {e['date']:<12}| {e['description']:<30}")

                    try:
                        raw = input("Enter Event #: ")
                        if raw.strip() == "":
                            print("Input cannot be empty.")
                            continue
                        index = int(raw) - 1
                    except ValueError:
                        print("Invalid input.")
                        continue

                    if 0 <= index < len(events):
                        e = events[index]
                        print(f"\nEditing Event: {e['title']} | {e['date']} | {e['description']}")

                        while True:
                            print("\nWhat would you like to edit?")
                            print("[1] Title")
                            print("[2] Date")
                            print("[3] Description")
                            print("[4] Done Editing")
                            edit_choice = input("Choose: ")

                            if edit_choice == "1":
                                new_title = input(f"Enter new title (leave blank to keep '{e['title']}'): ")
                                if new_title.strip() != "":
                                    e['title'] = new_title
                                    print("Title updated!")
                                else:
                                    print("Kept original title.")

                            elif edit_choice == "2":
                                new_date = input(f"Enter new date (leave blank to keep '{e['date']}'): ")
                                if new_date.strip() != "":
                                    e['date'] = new_date
                                    print("Date updated!")
                                else:
                                    print("Kept original date.")

                            elif edit_choice == "3":
                                new_desc = input(f"Enter new description (leave blank to keep '{e['description']}'): ")
                                if new_desc.strip() != "":
                                    e['description'] = new_desc
                                    print("Description updated!")
                                else:
                                    print("Kept original description.")

                            elif edit_choice == "4":
                                print("Finished editing this event.")
                                break

                        else:
                             print("Invalid choice.")
                    else:
                        print("Invalid Event #.")


                elif admin_choice == "4":
                    while True:
                        print("\n----- ARCHIVE DASHBOARD -----")
                        print("[1] Archive an Event")
                        print("[2] View Archived Events")
                        print("[3] Restore Archived Events")
                        print("[4] Back")
                        archive_choice = input("Choose: ")

                        if archive_choice == "1":
                            if not events:
                                print("No events to archive.")
                                continue
                            print("\nNo. | Event List               | Date        | Description")
                            print("-" * 70)
                            for i, e in enumerate(events, 1):
                                print(f"{i:<4}| {e['title']:<25}| {e['date']:<12}| {e['description']:<30}")

                            try:
                               index = int(input("Enter event # to archive: ")) - 1
                            except ValueError:
                                print("Invalid input.")
                                continue

                            if 0 <= index < len(events):
                                archived = events.pop(index)
                                archived_events.append(archived)
                                print(f"Archived '{archived['title']}'")
                            else:
                                print("Invalid Event #.")

                        elif archive_choice == "2":
                            if not archived_events:
                                print("No archived events.")
                                continue
                            print("\nNo. | Archived Event           | Date        | Description")
                            print("-" * 70)
                            for i, e in enumerate(archived_events, 1):
                                print(f"{i:<4}| {e['title']:<25}| {e['date']:<12}| {e['description']:<30}")
                            input("\nPress Enter to go back...")

                        elif archive_choice == "3":
                            if not archived_events:
                                print("No archived events to restore.")
                                continue
                            print("\nNo. | Archived Event           | Date        | Description")
                            print("-" * 70)
                            for i, e in enumerate(archived_events, 1):
                                print(f"{i:<4}| {e['title']:<25}| {e['date']:<12}| {e['description']:<30}")

                            try:
                                index = int(input("Enter event # to restore: ")) - 1
                            except ValueError:
                                print("Invalid input.")
                                continue

                            if 0 <= index < len(archived_events):
                                restored = archived_events.pop(index)
                                events.append(restored)
                                print(f"Restored '{restored['title']}' to active events.")
                            else:
                                print("Invalid Event #.")

                        elif archive_choice == "4":
                            break

                    else:
                        print("Invalid choice")

                elif admin_choice == "5":
                    break
                
                else:
                    print("Invalid choice")
        else:
            print("Invalid login")

    elif choice == "2":
        print("\n----- STUDENT VIEW -----")
        if not events:
            print("No events found.")
        else:
            for i, e in enumerate(events, 1):
                print(str(i) + ". " + e['title'] + " | " + e['date'] + " | " + e['description'])
        input("Press Enter to return...")

    elif choice == "3":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice")