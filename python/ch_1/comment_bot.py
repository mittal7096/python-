import os
import time
import random
import re

def main():
    print("Welcome to the auto comment bot.")
    time.sleep(2)
    print("This bot will automatically comment on given hashtag.")

    while True:
        print()
        print("Enter a hashtag:")
        hashtag = input()

        if not hashtag.startswith("#"):
            print("Please enter a valid hashtag.")
            continue

        if not os.path.exists("comments.txt"):
            print("File not found.")
            time.sleep(2)
            continue

        with open("comments.txt", "r") as f:
            comments = f.readlines()

        if len(comments) == 0:
            print("No comments found.")
            time.sleep(2)
            continue

        print("Enter the number of comments:")
        num_comments = int(input())

        for i in range(num_comments):
            comment = random.choice(comments)
            print("Commenting:", comment)
            os.system(f"instagram-scraper {hashtag} -u username -p password --maximum 100 --media-types none --comments -m 1 -q --template-path comments.txt")
            time.sleep(random.randint(5, 10))

if __name__ == "__main__":
    main()