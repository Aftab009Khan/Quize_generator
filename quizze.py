questions=[["what is best lang"
,"cpp","java","cp","py",4],
["what is frontend lang","py","java","cp","js",4
    ]]
ques=["what is best lang","what is frontend lang"]

score=0
levels=[10000,20000,50000,100000]
for i in range(len(questions)):
    question=questions[i]
    print(f"question for {levels[i]}")
    print(ques[i])
    print(f"a.{question[1]}   b.{question [2]}")
    print(f"c.{question[3]}   d.{question [4]}")
    reply=int(input('enter 1-4\n'))
    if reply==4:
        print("correct answer")
        print(f'won{levels[i]}')
    else:
        print('wrong answer ')
        print(f'lose{levels[i]}')
