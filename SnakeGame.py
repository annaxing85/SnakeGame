{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11240\viewh6620\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from processing import *\
import random\
\
\
def setup():\
  size(550, 350)\
  frameRate(40)\
  noStroke()\
  \
food_x=random.randint(0,500)\
food_y=random.randint(0,300)\
food_size=15\
\
snake_x=random.randint(0,500)\
snake_y=random.randint(0,300)\
snake_size=20\
\
r=random.randint(0,255)\
g=random.randint(0,255)\
b=random.randint(0,255)\
\
score=0\
\
gameover=False\
\
direction="R"\
\
\
def keyPressed():\
  global direction \
  if keyCode == 37: \
    direction = "L"\
    \
  if keyCode == 39:\
    direction = "R"\
    \
  if keyCode == 38:\
    direction = "U"\
  \
  if keyCode == 40:\
    direction = "D"\
\
def movesnake():\
  global snake_x, snake_y, direction\
  if direction == "R":\
    snake_x=snake_x + 3\
    \
  if direction == "L":\
    snake_x=snake_x - 3\
    \
  if direction == "U":\
    snake_y=snake_y - 3\
    \
  if direction == "D":\
    snake_y=snake_y + 3\
    \
    \
def drawfood():\
  fill(0, 230, 0) \
  rect(food_x,food_y,food_size,food_size)\
  \
def drawsnake():\
  fill(250, 250, 100)\
  rect(snake_x,snake_y,snake_size,snake_size)\
  \
def newfood():\
  global food_x, food_y, food_size\
  food_x=random.randint(0,500)\
  food_y=random.randint(0,300)\
  food_size=random.randint(5,snake_size)\
\
def FoodInSnake():\
  topleft = pointInRect(food_x,food_y,snake_x,snake_y,snake_size,snake_size)\
  topright = pointInRect(food_x + food_size,food_y,snake_x,snake_y,snake_size,snake_size)\
  bottomleft = pointInRect(food_x,food_y + food_size,snake_x,snake_y,snake_size,snake_size)\
  bottomright = pointInRect(food_x + food_size,food_y + food_size,snake_x,snake_y,snake_size,snake_size)\
  if topleft or topright or bottomleft or bottomright:\
    addscore()\
    newfood()\
    return True\
  else:\
    return False\
  \
def pointInRect(pt_x, pt_y, x, y, w, h): \
  if (pt_x > x) and (pt_x < x + w) and (pt_y > y) and (pt_y < y + h): \
    return True \
  else:\
    return False\
    \
def drawscore():\
  textSize(20)\
  fill(0,0,0)\
  text("Score: " + str(score),450,30)\
  \
def addscore():\
  global score\
  score=score + 1\
 \
  \
  \
def checkscreen():\
  global gameover\
  if snake_x < 0 or snake_x > 550 or snake_y < 0 or snake_y >350:\
    background(r,g,b)\
    textSize(50)\
    fill(0,0,0)\
    text("GAME OVER",550/2-140,350/2)\
    gameover=True\
\
    \
def draw():\
  if gameover==False:\
    background(100, 150, 200)\
    drawfood()\
    drawsnake()\
    movesnake()\
    FoodInSnake()\
    drawscore()\
    checkscreen()\
  else:\
    background(r,g,b)\
    textSize(50)\
    fill(0,0,0)\
    text("GAME OVER",550/2-140,350/2)\
  \
run()\
\
\
\
\
\
\
\
\
\
}