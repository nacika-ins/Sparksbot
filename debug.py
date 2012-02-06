#!/home/nacika/.virtualenvs/akicansoft/bin/python
# -*- coding: utf-8 -*-
#ver. 0.5 β
import google
import time
import logging
import re
import random
import sys
import traceback



#デバッグするかどうか
DEBUG = False

def main():

    #Googleにログイン
    #print "ログインしています"
    g = google.Login("", "")
    if not DEBUG:
        
        #Release
        plus = g.plus("102572631772607977847") #102572631772607977847 #115513203631682315448
    else:
        #Debug
        plus = g.plus("107783647697859888499")
    
    #print "Google+を使えるようにしています"
    post = plus.post()

    #除外する正規表現
    ngwrd = re.compile(r"(超展開|ドメサカ板まとめブログ|二次嫁|社説|VIPPER|暇人＼\(\^o\^\)／速報|２ちゃんねる|はちま起稿|やらおん|キムチ速報|まとめたニュース|あじゃじゃしたー|ぶる速|エイガドットコム|ナルシマツトム|ツンダオワタ情報|笑[ ]韓[ ]ブログ|Hatena::Group::onlooker::2ch-Dojin|アルファルファモザイクだった|VIPPERな俺|暇人＼\(\^o\^\)／速報|ぁゃιぃ\(*゜ー゜\)NEWS 2nd|とりのまるやき|育児板拾い読み＠２ｃｈ|ハムスター速報|ぶる速-VIP|続・妄想的日常|【2ch】ニュー速VIPブログ\(`・ω・´\)|ゴールデンタイムズ|SLPY|Blogger Alliance | 404 Not Found|がぞ～速報|2chコピペ保存道場|unt    site|【2ch】ニュー速クオリティ|痛いニュース\(ノ∀`\)|403 Error - FC2Blog|スチーム速報　ＶＩＰ|無題のドキュメント 旧館|わくてか速報|カゼタカ2ブログch|世界って広くね\(；゜Д゜\)|画像スレとらのあな|すくいぬ|ニダー速報|VIPワイドガイド|プラティカルパ|みんくちゃんねる|競馬2ちゃんねる＠ブログ|ヴィブロ|２ちゃん的韓国ニュース|常識的に考えた|旧はちま起稿|芸スポまとめblog|未定なブログ|仲間にゅーす|2Tunes|Witch Hunting Girlscouts|うらやましからん|喪ゲ女|戯言ニュース|青い空は大嫌いだ水色の空は大好きだ|こっちは必死なんだよ|デジタルニューススレッド|Blogger Alliance | 404 Not Found|クソスレドンキーノ|あにめちゃんねる|WWW.ニュース|サカ速|うるさい黙れ|特設ニュースちゃんねる|ニュー投|喪男のまとめ切れない事。|ニュースかしら|日本ってすごくね\(；゜Д゜\)|キラ速-KIRA☆SOKU-|痛ニュー速報！|キリンちゃんねる|コピペ運動会|ねがすぱ|もみあげチャ～シュ～|オレ的ゲーム速報＠刃|まとめたニュース|山師ニュース＼\(\^o\^\)／|Syu’s quiz blog|にしみーぶろぐ|ねとねた|Blogger Alliance | 404 Not Found|たん速|のとーりあす|丁寧語とか、礼儀正しく書いてみる日記２|ニュース速報プラチナム|茶速|ゆめみがちサロン|イフカルト|電撃速報|2chドロッペ\(。・-・\)|とてつもなく日本|あんか～びっぷ|アフォニュース|君のてのひらから|やる夫ネット|やく速|xxxxx.jpg|無題ブログ|Life Insurance|噂のジョニー|twospo|時は来た！それだけだ|バイク板＆車板まとめブログ|Blogger Alliance | 404 Not Found|ぷん太のにゅーす|カナ速mini|ニュースウォッチ２ちゃんねる -NW2-|秒速ニューろぐ|チラシの裏は真空パック - FC2 BLOG パスワード認証|ねら速|無駄な知識などない|フライドチキンは空をとぶ -フラソラ-|ゲーム板見るよ！|めでたしめでたし|わんこと|あの日の過ち、今日の過ち|一般書籍＠2ch掲示板お勧め自己啓発書　のまとめブログ|面白蛇屋|グロリアン|グロカルト|ドルジのあれこれ|FF35しようずｗｗｗｗｗｗｗｗ|2ch ニュース速報＋ ダイジェスト|市況版、天使と悪魔と断末魔|Blogger Alliance | 404 Not Found|コピペ馬鹿 ～創造力の欠如～|２記|川の流れのようなチラシの裏|東京エスノ|もうだめだ|V速ニュップ|SS宝庫～みんなの暇つぶし～|まめのぐ 第二幕 跡地|クズ速報|インフル速報|ぐる速|ムズ痒いブログ|basicchannel|２ちゃん競馬情報ニュース|A6ニュース\(゜Д゜\)|２のニュース)")
    ngurl = re.compile(r"(chaos2ch\.com|blog\.livedoor\.jp/nwknews|nureinu\.net|football-2ch\.com|blog\.livedoor\.jp/kinisoku|blog\.livedoor\.jp/himasoku123|honwaka2ch\.livedoor\.biz)")
    
    #ログリストの生成
    #print "ログリストを生成しています"
    loglist = []
    if 1:
        act = plus.activity("", 40)
        
        for i in range(act.length()):
            title = act.sparkstitle(i)
            if title:
                loglist.append(title)

    #print "loglist: "
    #print loglist
    if len(loglist) == 0:
        logging.error("ログが無効です")
        return
        
    #print "ループに入ります"
    while(1):
        
        #投稿フラグ
        postflag = 0
        
        #検索しています
        #print "検索しています"
        search = plus.search("あ|い|う|え|お|か|き|く|け|こ|さ|し|す|せ|そ|た|ち|つ|て|と|な|に|ぬ|ね|の|は|ひ|ふ|へ|ほ|ま|み|む|め|も|や|ゆ|よ|ら|り|る|れ|ろ|わ|を|ん", "sparks", "all", "new")

        #ポストの取得
        l = search.length()
        if l == 0 : 
            wait = random.randint(30, 40)
            #print str(wait)+"分待機中"
            time.sleep(60*wait)
        
        for i in range(l):

            #すでに投稿したものだった場合無視
            title = search.sparkstitle(i)
            
            #無い場合飛ばす
            if title == "":
                continue

            #NG正規表現が含まれている場合
            try:
                if ngurl.search(search.sparkslink(i)).group(1):
                    #print "NGURLが含まれていました: "+search.sparkslink(i)
                    continue
            except:
                pass

            #NG正規表現が含まれている場合
            try:
                if ngwrd.search(title).group(1):
                    #print "NGワードが含まれていました: "+search.sparkslink(i)
                    continue
            except:
                pass

            #NG正規表現が含まれている場合
            try:
                if ngwrd.search(search.sparksauther(i)).group(1):
                    #print "NGワードが含まれていました: "+search.sparkslink(i)
                    continue
            except:
                pass
            
            flag = 0
            for ii in loglist:
                
                #一致
                if ii == title:
                    flag = 1
                    break
                
            #一致時の実装
            if flag == 1:
                #print "すでに投稿されたものです: "+search.sparkslink(i)
                continue

            #含まれていない場合実行
            #print "ユーザー名: "+search.postusername(i)
            #print "ユーザーID: "+search.postuserid(i)
            #print "本文: "+search.postbody(i)
            #print "コメント数: "+str(search.commentlength(i))
            #print "再共有数: "+str(search.sharelength(i))
            #print "+1数: "+str(search.plusonelength(i))
            #print "ポストID: "+search.postid(i)
            #print "SparksID: "+search.sparksid(i)
            #print "----------------------------------------"
            
            #投稿
            post.sparks("", search.sparksid(i))
            postflag = 1
            #print "投稿しました: "+search.permalink(i)
            
            #10〜15分待つ
            wait = random.randint(10, 15)
            #print str(wait)+"分待機中"
            time.sleep(60*wait)
            
            #ログに追加する
            loglist.append(title)
            
            #ログの肥大化を防止
            if len(loglist) >= 1000:
                loglist = loglist[1:]
        
        #投稿しなかった場合
        if not postflag:

            #10〜15分待つ
            wait = random.randint(10, 15)
            #print str(wait)+"分待機中"
            time.sleep(60*wait)

if __name__ == '__main__':
    #エラーのときは再起動する
    if DEBUG:
        main()
    else:
        while(1):
            try:
                main()
                logging.error("30分待機中")
                time.sleep(60*30)
                logging.error("再起動しています")
            except:
                info = sys.exc_info()
                tbinfo = traceback.format_tb( info[2] )
                for tbi in tbinfo:
                    logging.error(tbi)
                logging.error("%s\n-----------------------------------------------"% str( info[1] ))
                logging.error("30分待機中")
                time.sleep(60*30)
                logging.error("再起動しています")
                continue
        