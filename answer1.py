def main():
    
    value = 10
    n = 0
    bintang = ''
    for i in range(1,11):
        n = value - i
        space =' '*n
        bintang +='*'
        print(space+bintang)

if __name__ == "__main__":
      main()