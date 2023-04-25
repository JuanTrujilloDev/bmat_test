from csv_utils import GroupSongsPlaysPerDay

if __name__ == "__main__":
    file_dir = "songs.csv"
    GroupSongsPlaysPerDay().generate_csv(file_dir)
