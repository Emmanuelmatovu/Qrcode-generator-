import os

import qrcode
import time



try:

    url = input("enter url e.g https://www.google.com/download: ")
    while url.startswith("https") and not url.isspace():
        filename = input("enter filename e.g qrcode.png: ")
        if os.path.exists(filename):
            print("file exists")
            quit()
        elif filename.endswith(".png"):
            qrcode.make(url).save(filename)
            print("file saved")
            quit()
        else:
            print("must end in .png")
            print("please try again")
            continue
        break




except KeyboardInterrupt:
    print("user interruption error from keyboard")
except Exception as e:
    print(e)
finally:
    print("closing program......")

    ask=input("do u want to continue? (yes/no): ")
    if ask == "yes":
        try:

            url = input("enter url e.g https://www.google.com/download: ")
            while url.startswith("https") and not url.isspace():
                filename = input("enter filename e.g qrcode.png: ")
                if os.path.exists(filename):
                    print("file exists")
                    quit()
                elif filename.endswith(".png"):
                    qrcode.make(url).save(filename)
                    print("file saved")
                    quit()
                else:
                    print("must end in .png")
                    print("please try again")
                    continue
                break




        except KeyboardInterrupt:
            print("user interruption error from keyboard")
        except Exception as e:
            print(e)
        finally:
            for t in range(1,10):
                time.sleep(1)
                print("closing program......")



            print("program finished with exit code 0")


    else:
        for t in range(1, 10):
            time.sleep(1)
            print("closing program in......")

        print("program finished with exit code 0")



