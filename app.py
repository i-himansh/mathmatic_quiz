with open("questions.txt" , "r") as my_file:
    files = [file.strip() for file in my_file.readlines()]
   # print(files)

score = 0
total = len(files)

for line in files:
    q , a = line.split("=")
    ans = input(f"{q}=")

    if ans == a :
        score +=1
with open("result.txt" , "w")as result:
    result.write(f"your final score is {score}/{total}")

