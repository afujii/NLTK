
with open('./hyakuninUTF8.txt','r',encoding='UTF8') as fp:
  utas = fp.readlines()

head  = utas.pop(0)# utas は、No.1 からの全データ（list）になる。
#kamis = [uta.split(',')[4] for uta in utas ] # 上の句(かな）
#simos = [uta.split(',')[5] for uta in utas ] #下の句（かな）

from random import choice
import re
#target = choice(utas)
target = utas[0]
kami = target.split(',')[4]
simo = target.split(',')[5].strip('\n')
display = list('□'*len(simo))

guessed_letters = []
guessed_words = []

tries = 10
    
guessed = False
while not guessed and tries > 0:
  print(''.join(display))
  guess = input("「"+kami+"」: ")
  if len(guess) == 1: # 一文字の推理
    if guess in guessed_letters:
      print("その文字は既に試しました。")
    elif guess not in simo:
      print(guess, "は含まれていません")
      tries -= 1
      guessed_letters.append(guess)
    else:
      print("ナイス",guess,"は、含まれている文字です。")
      guessed_letters.append(guess)
      word_as_list = list(display) 
      indices = [i for i, letter in enumerate(simo) if letter== guess] # 上記解説
      for index in indices:
        word_as_list[index] = guess
      display = "".join(word_as_list)
      if "□" not in display:
        guessed = True # 推理の修了条件
  elif len(guess) == len(simo):#　句の推理
    if guess in guessed_words:
      print("その言葉は既に試して、はずれてます。")
    elif guess != simo:
      print("その句ではありません。")
      tries -= 1
      guessed_words.append(guess)
    else:
      guessed = True
      print("できました")
      display = simo 
  else:
    print("不当な入力です（文字か単語を入れる）")
