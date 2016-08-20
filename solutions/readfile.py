import sys

# def main == private int main()

def main(args): # args is the same as sys.argv[1:]
   print args 
   filename = args[0] # python is zero index
   with open(filename) as f: # f is the object that contains the file contents
       for line in f:
           print line.strip() + "  HI JUYA!!!" 
   print "Hi Juya!!!"

if __name__ == "__main__":
    print sys.argv
    main(sys.argv[1:])
