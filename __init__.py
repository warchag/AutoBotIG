from bot import *
if __name__ == "__main__":
    hashtags = input("=== input your tag ===\n")
    downloadcount = int(input("=== input your downloadcount ===\n"))
    MYBOT = Instargram("user","password")
    MYBOT.Login()
    MYBOT.Search_Tag(hashtags)
    MYBOT.Like_photo(downloadcount,hashtags)
