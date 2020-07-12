# A.請寫一個程式把裡面字串反過來
# B.請寫一個程式把裡面字串,每個單子本身做反轉,但單字的順序不變
# f("junyiacademy" ) == "ymedacaiynuj"
# f("flipped class room is important") == "deppilf ssalc moor si tnatropmi"

def main(str):
    strlist=[x[::-1] for x in str.split()]
    return " ".join(strlist)

if __name__ =="__main__":
  print(main(input("請輸入：")))