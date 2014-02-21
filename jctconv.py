# -*- coding: utf-8 -*-
import unicodedata
"""
jctconv 0.0.6 - 全角・半角・ひらがな・カタカナ等相互変換モジュール

Author:
	Yukino Ikegami

Lisence:
	MIT License

Usage:
	import jctconv
	text = jctconv.hira2kata(text, [ignore]) # ひらがなを全角カタカナに変換
	text = jctconv.hira2hkata(text, [ignore]) # ひらがなを半角カタカナに変換
	text = jctconv.kata2hira(text, [ignore]) # 全角カタカナをひらがなに変換
	text = jctconv.h2z(text, [mode, ignore]) # 半角文字を全角文字に変換
	text = jctconv.z2h(text, [mode, ignore]) # 全角文字を半角文字に変換
	text = jctconv.normalize(text, [nomalizemode]) # 半角カナを全角カナへ、全角英数字を半角英数字に変換

	modeで変換対象文字種(ALL, ASCII, DIGIT, KANA)を組み合わせて指定可能
	nomalizemodeはNFC, NFKC, NKD, NFKDから指定可能
	ignoreで変換除外文字を指定可能
"""

HIRAGANA = list(u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔ')

HALF_ASCII = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~',' ']
HALF_DIGIT = ['0','1','2','3','4','5','6','7','8','9']
HALF_KANA_SEION = list(u'ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶ')
HALF_KANA = [u'ｧ',u'ｱ',u'ｨ',u'ｲ',u'ｩ',u'ｳ',u'ｪ',u'ｴ',u'ｫ',u'ｵ',u'ｶ',u'ｶﾞ',u'ｷ',u'ｷﾞ',u'ｸ',u'ｸﾞ',u'ｹ',u'ｹﾞ',u'ｺ',u'ｺﾞ',u'ｻ',u'ｻﾞ',u'ｼ',u'ｼﾞ',u'ｽ',u'ｽﾞ',u'ｾ',u'ｾﾞ',u'ｿ',u'ｿﾞ',u'ﾀ',u'ﾀﾞ',u'ﾁ',u'ﾁﾞ',u'ｯ',u'ﾂ',u'ﾂﾞ',u'ﾃ',u'ﾃﾞ',u'ﾄ',u'ﾄﾞ',u'ﾅ',u'ﾆ',u'ﾇ',u'ﾈ',u'ﾉ',u'ﾊ',u'ﾊﾞ',u'ﾊﾞ',u'ﾋ',u'ﾋﾞ',u'ﾋﾞ',u'ﾌ',u'ﾌﾞ',u'ﾌﾞ',u'ﾍ',u'ﾍﾞ',u'ﾍﾞ',u'ﾎ',u'ﾎﾞ',u'ﾎﾞ',u'ﾏ',u'ﾐ',u'ﾑ',u'ﾒ',u'ﾓ',u'ｬ',u'ﾔ',u'ｭ',u'ﾕ',u'ｮ',u'ﾖ',u'ﾗ',u'ﾘ',u'ﾙ',u'ﾚ',u'ﾛ',u'ﾜ',u'ｦ',u'ﾝ',u'ｰ',u'ヮ',u'ヰ',u'ヱ',u'ヵ',u'ヶ',u'ｳﾞ']
FULL_ASCII = list(u'！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～　')
FULL_DIGIT = list(u'０１２３４５６７８９')
FULL_KANA = list(u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ')
FULL_KANA_SEION = list(u'ァアィイゥウェエォオカキクケコサシスセソタチッツテトナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶ')
H2K_TABLE = dict(zip([ord(char) for char in HIRAGANA], FULL_KANA))
H2HK_TABLE = dict(zip([ord(char) for char in HIRAGANA], HALF_KANA))

K2H_TABLE = dict(zip([ord(char) for char in FULL_KANA], HIRAGANA))

H2Z_A = dict(zip([ord(char) for char in HALF_ASCII], FULL_ASCII))
H2Z_AD = dict(zip([ord(char) for char in HALF_ASCII+HALF_DIGIT], FULL_ASCII+FULL_DIGIT))
H2Z_AK = dict(zip([ord(char) for char in HALF_ASCII+HALF_KANA_SEION], FULL_ASCII+FULL_KANA_SEION))
H2Z_D = dict(zip([ord(char) for char in HALF_DIGIT], FULL_DIGIT))
H2Z_K = dict(zip([ord(char) for char in HALF_KANA_SEION], FULL_KANA_SEION))
H2Z_DK = dict(zip([ord(char) for char in HALF_DIGIT+HALF_KANA_SEION], FULL_DIGIT+FULL_KANA_SEION))
H2Z_ALL = dict(zip([ord(char) for char in HALF_ASCII+HALF_DIGIT+HALF_KANA_SEION], FULL_ASCII+FULL_DIGIT+FULL_KANA_SEION))

Z2H_A = dict(zip([ord(char) for char in FULL_ASCII], HALF_ASCII))
Z2H_AD = dict(zip([ord(char) for char in FULL_ASCII+FULL_DIGIT], HALF_ASCII+HALF_DIGIT))
Z2H_AK = dict(zip([ord(char) for char in FULL_ASCII+FULL_KANA], HALF_ASCII+HALF_KANA))
Z2H_D = dict(zip([ord(char) for char in FULL_DIGIT], HALF_DIGIT))
Z2H_K = dict(zip([ord(char) for char in FULL_KANA], HALF_KANA))
Z2H_DK = dict(zip([ord(char) for char in FULL_DIGIT+FULL_KANA], HALF_DIGIT+HALF_KANA))
Z2H_ALL = dict(zip([ord(char) for char in FULL_ASCII+FULL_DIGIT+FULL_KANA], HALF_ASCII+HALF_DIGIT+HALF_KANA))

# ひらがなから全角カタカナへ
def hira2kata(text, ignore=''):
	h2k_hash = _update_ignorechar(ignore, H2K_TABLE)
	return _convert(text, h2k_hash)
# hira2kataの別名
def H2K(text, ignore=''):
	return hira2kata(text, ignore)

# ひらがなから半角ｶﾀｶﾅへ
def hira2hkata(text, ignore=''):
	h2hk_hash = _update_ignorechar(ignore, H2HK_TABLE)
	return _convert(text, h2hk_hash)
# hira2hkataの別名
def H2hK(text, ignore=''):
	return hira2hkata(text, ignore)

# 全角カタカナからひらがなへ
def kata2hira(text, ignore=''):
	k2h_hash = _update_ignorechar(ignore, K2H_TABLE)
	return _convert(text, k2h_hash)
# kata2hiraの別名
def K2H(text, ignore=''):
	return kata2hira(text, ignore)

# 半角から全角へ
def h2z(text, mode='KANA', ignore=''):
	if mode == 'ALL':
		h2z_hash = H2Z_ALL
		text = _h2z_dakuten(text)
	else:
		if 'ASCII' in mode:
			if 'DIGIT' in mode:
				if 'KANA' in mode:
					h2z_hash = H2Z_ALL
					text = _h2z_dakuten(text)
				else:
					h2z_hash = H2Z_AD
			elif 'KANA' in mode:
				h2z_hash = H2Z_AK
				text = _h2z_dakuten(text)
			else:
				h2z_hash = H2Z_A
		elif 'DIGIT' in mode:
			if 'KANA' in mode:
				h2z_hash = H2Z_DK
				text = _h2z_dakuten(text)
			else:
				h2z_hash = H2Z_D
		else:
			h2z_hash = H2Z_K
			text = _h2z_dakuten(text)
	h2z_hash = _update_ignorechar(ignore, h2z_hash)
	return _convert(text, h2z_hash)

# 全角から半角へ
def z2h(text, mode='KANA', ignore=''):
	if mode == 'ALL':
		z2h_hash = Z2H_ALL
	else:
		if 'ASCII' in mode:
			if 'DIGIT' in mode:
				if 'KANA' in mode:
					z2h_hash = Z2H_ALL
				else:
					z2h_hash = Z2H_AD
			elif 'KANA' in mode:
				z2h_hash = Z2H_AK
			else:
				z2h_hash = Z2H_A
		elif 'DIGIT' in mode:
			if 'KANA' in mode:
				z2h_hash = Z2H_DK
			else:
				z2h_hash = Z2H_D
		else:
			z2h_hash = Z2H_K
	z2h_hash = _update_ignorechar(ignore, z2h_hash)
	return _convert(text, z2h_hash)

# 半角カナを全角カナへ、全角英数字を半角英数字へ
# (unicodedataの全角WAVE DASH等も半角に正規化する)
def normalize(text, mode='NFKC', ignore=''):
	text = text.replace(u'〜',u'ー').replace(u'～',u'ー')
	text = text.replace(u"’","'").replace(u'”','"').replace(u'“','``')
	text = text.replace(u'―','-').replace(u'‐',u'-')
	return unicodedata.normalize(mode,text)

# 変換除外文字の反映
def _update_ignorechar(ignore, conv_hash):
	for character in ignore:
		conv_hash[ord(character)] = character
	return conv_hash

# 半角濁点カナを全角に変換
def _h2z_dakuten(text):
	return text.replace(u"ｶﾞ",u"ガ").replace(u"ｷﾞ",u"ギ").replace(u"ｸﾞ",u"グ").replace(u"ｹﾞ",u"ゲ").replace(u"ｺﾞ",u"ゴ").replace(u"ｻﾞ",u"ザ").replace(u"ｼﾞ",u"ジ").replace(u"ｽﾞ",u"ズ").replace(u"ｾﾞ",u"ゼ").replace(u"ｿﾞ",u"ゾ").replace(u"ﾀﾞ",u"ダ").replace(u"ﾁﾞ",u"ヂ").replace(u"ﾂﾞ",u"ヅ").replace(u"ﾃﾞ",u"デ").replace(u"ﾄﾞ",u"ド").replace(u"ﾊﾞ",u"バ").replace(u"ﾋﾞ",u"ビ").replace(u"ﾌﾞ",u"ブ").replace(u"ﾍﾞ",u"ベ").replace(u"ﾎﾞ",u"ボ").replace(u"ﾊﾟ",u"パ").replace(u"ﾋﾟ",u"ピ").replace(u"ﾌﾟ",u"プ").replace(u"ﾍﾟ",u"ペ").replace(u"ﾎﾟ",u"ポ").replace(u"ｳﾞ",u"ヴ")

# ハッシュで文字を変換
def _convert(text, conv_hash):
	#	print conv_hash
	return text.translate(conv_hash)
	#return ''.join([conv_hash.get(character,character) for character in text])

if __name__ == '__main__':
	print(hira2kata(u'ともえまみ'))
	print(hira2hkata(u'ともえまみ'))
	print(kata2hira(u'巴マミ'))
	print(h2z(u'ﾃｨﾛﾌｨﾅｰﾚ'))
	print(z2h(u'ティロフィナーレ'))
	print(normalize(u'ティロ･フィナ〜レ','NFKC'))
