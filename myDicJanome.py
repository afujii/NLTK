# https://zenn.dev/megane_otoko/articles/055_janome_user_dictionary

from janome.tokenizer import Tokenizer

t = Tokenizer()    
t = Tokenizer("./myDicUTF8.csv", udic_type="simpledic", udic_enc="UTF8")

for token in t.tokenize('あきのたのかりほのいほのとまをあらみわがころもでにゆきはふりつつ'):
    print(token)

#　辞書の作成・利用には注意を要する。文字コードの不用意な変換、拡張子には注意。
# マイ辞書を利用した分かち書きを用意する。
