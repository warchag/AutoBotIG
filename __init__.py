from bot import *
if __name__ == "__main__":
    hashtags = input("=== input your tag ===")
    downloadcount = int(input("=== input your downloadcount ==="))
    MYBOT = Instargram("warchag01","Billkyz131")
    MYBOT.Login()
    MYBOT.Search_Tag(hashtags)
    MYBOT.Like_photo(downloadcount)