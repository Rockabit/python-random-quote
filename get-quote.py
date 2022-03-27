def main():
  print("Keep it logically awesome.")

  f = open("best_quote.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

if __name__== "__main__":
  main()
