def main(num):
    bag_i = ['pencil']
    bag_j = ['ball point pen']
    bag_k = ['pencil','ball point pen']
    bags = [bag_i,bag_j,bag_k]
    try:
        if len(bags[num-1]) == 1 and bag_i[0] == bag_k[num-1]:
            return '這個袋子只裝鉛筆，其他二個袋子，一個只裝原子筆，另一個有鉛筆也有原子筆。'
        if len(bags[num-1]) == 1 and bag_j[0] == bag_k[num-1]:
            return '這個袋子只裝原子筆，其他二個袋子，一個只裝鉛筆，另一個有鉛筆也有原子筆。'
        if len(bags[num-1])==2:
            return '這個袋子有鉛筆也有原子筆，其他二個裝子，一個只裝鉛筆，另一個只裝原子筆。'
    except:
        return main(eval(input("請輸入號碼 1-3:")))

if __name__ == "__main__":
    result = main(eval(input("請輸入號碼 1-3:")))
    print(result)
