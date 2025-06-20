import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()


cursor.execute(
    """
                    CREATE TABLE IF NOT EXISTS videos(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        time TEXT NOT NULL
                    )
               """
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES  (?, ?)", (name, time))
    con.commit()


def update_video(new_name, new_time, video_id):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def delete_video(delete_video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (delete_video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. exit app")

        choice = input("Enter you choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(name, time, video_id)
        elif choice == "4":
            delete_video_id = input("Enter the video ID to delete: ")
            delete_video(delete_video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

    con.close()


if __name__ == "__main__":
    main()
