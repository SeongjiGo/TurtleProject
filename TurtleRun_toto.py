from turtle import *
from random import randint
import time as t

title("Who is TurtleRunGame winner?")
listen()
color("Orange")
#스코어 관련
score = [0, 0, 0, 0]
scoreCheck = Turtle() 
scoreCheck.hideturtle()
scoreCheck.speed(0)
scoreCheck.penup()

#성공률 관련
strike = Turtle() #출력하기 위한 터틀
strike.speed(0)
gameNum = 1 #경기횟수
strikeProbability = 0.0 # 적중률
winnerNum = 0 #승리 거북이 번호
strikeNum = 0 #적중 횟수
missNum = 0 #미스 횟수
selectNum = 0 #배팅할 거북이 숫자 (1:하늘 2:흰색 3:핑크 4:빨강)

#달리기 레이스 배경
bgcolor('black')
speed(0)
penup()
hideturtle()
goto(-150, 200)
showturtle()
write("Who is winner?\n20185103 고성지", move=False, font = ("Arial", 40, "normal"))
goto(-280, 140)

for step in range(20):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(30)

########################################################### 함수들 #####################################################################################
def init():
    global gameNum
    gameNum += 1
    gubby.penup()
    gummy.penup()
    third.penup()
    fourth.penup()
    
    gubby.clear()
    gummy.clear()
    third.clear()
    fourth.clear()
    
    gubby.goto(-300, -200)
    gummy.goto(-100, -200)
    third.goto(100, -200)
    fourth.goto(300, -200)
    printScore()
    printStrike()
    
def up():
    setheading(90)
    forward(10)

def down():
    setheading(-90)
    forward(10)

def right():
    setheading(0)
    forward(10)

def left():
    setheading(180)
    forward(10)

def space():
    global gameNum
    global selectNum
    if((xcor() >= -310.0 and xcor() <= -290.0) and (ycor() >= -210.0 and ycor() <= -190.0)): #하늘색 거북이를 선택한 경우    
        gubby.right(360)
        selectNum = 1
        gubby.write("----날 선택해줘서 고마워..!")
        ontimer(play, 3000)

    if((xcor() >= -110.0 and xcor() <= -90.0) and (ycor() >= -210.0 and ycor() <= -190.0)): #핑크색 거북이를 선택한 경우
        selectNum = 2
        gummy.right(360)
        gummy.write("----자신이 없어요.. 질 자신이")
        ontimer(play, 3000)

    if((xcor() >= 90.0 and xcor() <= 110.0) and (ycor() >= -210.0 and ycor() <= -190.0)): #핫핑크색 거북이를 선택한 경우
        selectNum = 3
        third.right(360)
        third.write("----포기가 뭐죠?")
        ontimer(play, 3000)

    if((xcor() >= 290.0 and xcor() <= 310.0) and (ycor() >= -210.0 and ycor() <= -190.0)): #보라색 거북이를 선택한 경우
        selectNum = 4
        fourth.right(360)
        fourth.write("----괜히 빨강색이 아니죠")
        ontimer(play, 3000)

def play(): #경주 시작
    global winnerNum
    gubby.goto(-300, 100)
    

    gummy.goto(-300, 70)
    

    third.goto(-300, 40)
    

    fourth.goto(-300, 10)

    fourth.pendown()
    gubby.pendown()
    third.pendown()
    gummy.pendown()

    time = 0
    randSpeed = [randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)]
   
    while True:
        if time % 80 == 0 :
            randSpeed = [randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)]
            
        time += 1
        print(time)
        
        if(randint(1, 5) <= randSpeed[0]): #극적인 역전을 연출하기 위함
            gubby.forward(randint(1, 5))
    
        if(randint(1, 5) <= randSpeed[1]):
            gummy.forward(randint(1, 5))

        if(randint(1, 5) <= randSpeed[2]):
            third.forward(randint(1, 5))

        if(randint(1, 5) <= randSpeed[3]):
            fourth.forward(randint(1, 5))

        if (gubby.xcor() >= 290.0) : # 하늘색 거북이가 이긴 경우
            gubby.write("ㄴ..내가 이기다니! ㅜnㅜ", move=False, font=("Arial", 12, "normal"))
            score[0] += 1
            winnerNum = 1
            break;

        elif (gummy.xcor() >= 290.0) : # 핑크색 거북이가 이긴 경우
            gummy.write("아.. 봐주면서 할껄 :)", move=False, font=("Arial", 12, "normal"))
            score[1] += 15
            winnerNum = 2
            break;
    
        elif (third.xcor() >= 290.0) : # 핫핑크색 거북이가 이긴 경우
            third.write("쉽다쉬워!", move=False, font=("Arial", 12, "normal"))
            score[2] += 1
            winnerNum = 3
            break;
    
        elif (fourth.xcor() >= 290.0) : # 보라색 거북이가 이긴 경우
            fourth.write("역시 빨간색이 주인공이지!", move=False, font=("Arial", 12, "normal"))
            score[3] += 1
            winnerNum = 4
            break;
    strikeCal()
    ontimer(init, 2000)

def printScore(): # 거북이 승리횟수
    scoreCheck.clear()
    scoreCheck.showturtle()
    scoreCheck.color("skyblue")
    scoreCheck.goto(-400, 300)
    scoreCheck.write("하늘거북이가 이긴 횟수: {0}".format(score[0]), move=False, font=("Arial", 12, "normal"))

    scoreCheck.color("pink")
    scoreCheck.goto(-400, 280)
    scoreCheck.write("흰색거북이가 이긴 횟수: {0}".format(score[1]), move=False, font=("Arial", 12, "normal"))

    scoreCheck.color("violet")
    scoreCheck.goto(-400, 260)
    scoreCheck.write("핑크거북이가 이긴 횟수: {0}".format(score[2]), move=False, font=("Arial", 12, "normal"))

    scoreCheck.color("Red")
    scoreCheck.goto(-400, 240)
    scoreCheck.write("빨강거북이가 이긴 횟수: {0}".format(score[3]), move=False, font=("Arial", 12, "normal"))

    scoreCheck.hideturtle()

def strikeCal(): #적중관련 계산
    global selectNum
    global winnerNum
    global strikeNum
    global strikeProbability
    global gameNum
    
    if selectNum == winnerNum :
        strikeNum += 1

    strikeProbability = strikeNum / gameNum #적중률
 
def printStrike(): #적중관련 출력
    strike.clear()
    strike.showturtle()
    strike.penup()
    strike.color('green')
    strike.goto(420, 300)
    strike.write("적중횟수: {0}".format(strikeNum), move=False, font=("Arial", 24, "normal"))
    strike.goto(420, 250)
    strike.write("적중률: {0}".format(strikeProbability), move=False, font=("Arial", 24, "normal"))
    strike.goto(420, 200)
    strike.write("게임 횟수: {0}".format(gameNum-1), move=False, font=("Arial", 24, "normal"))
    strike.hideturtle()
#######################################################################################################################################################################################################
    
#거북이들 생성
gubby = Turtle()
gubby.color('skyblue')
gubby.shape('turtle')
gubby.penup()
gubby.goto(-300, -200)

gummy = Turtle()
gummy.color('pink')
gummy.shape('turtle')
gummy.penup()
gummy.goto(-100, -200)

third = Turtle()
third.color('violet')
third.shape('turtle')
third.penup()
third.goto(100, -200)

fourth = Turtle()
fourth.color('Red')
fourth.shape('turtle')
fourth.penup()
fourth.goto(300, -200)

printScore() #스코어 출력
printStrike() 
color("green")
goto(0, -300)
speed(None)
write("어느 거북이가 승리할까요?\n(방향키로 다가간 후 스페이스바)", move=False, font=("Arial", 20, "normal"))

onkeypress(up, "Up")
onkeypress(down, "Down")
onkeypress(right, "Right")
onkeypress(left, "Left")
onkeypress(space, "space")
