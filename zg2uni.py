# -*- coding: utf-8 -*-
import re


def convert(input):

    tallAA = u'\u102B'
    AA = u'\u102C'
    vi = u'\u102D'

    # lone gyi tin
    ii = u'\u102E'
    u = u'\u102F'
    uu = u'\u1030'
    ve = u'\u1031'
    ai = u'\u1032'
    ans = u'\u1036'
    db = u'\u1037'
    visarga = u'\u1038'

    asat = u'\u103A'

    ya = u'\u103B'
    ra = u'\u103C'
    wa = u'\u103D'
    ha = u'\u103E'
    zero = u'\u1040'

# replace for each zawgyi code to unicode character
	
    output = input

    output = output.replace(u'\u106A', u'\1009') # nya_lay_to_nya_gyi

    output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]', u'\u103C', output) # ya_yit
    output = re.sub(u'(\u103A)(\u1037)', u"\\2\\1", output);
    output = output.replace(u'\u103A\u1037', u'\u1037\u103A')
    output = output.replace(u'\u1075', u'\u1039\u1012')

    output = re.sub(u'\u106b', u'\u100a', output) # nya
    output = re.sub(u'\u1039', u'\u103a', output) # nga_thet
    output = re.sub(u'\u1086', u'\u103f', output) # tha_gyi
    output = re.sub(u'\u1033', u'\u102f', output) # ta_chaung_ngyin
    output = re.sub(u'\u1034', u'\u1030', output) # nat_chaung_ngyin
    output = re.sub(u'[\u103d\u1087]', u'\u103e', output) # hat_htoe
    output = re.sub(u'\u103c', u'\u103d', output) # wa_swal
    output = re.sub(u'[\u103a\u107d]', u'\u103b', output) # ya_pint
    output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037', output) # aut_myit
    output = re.sub(u'\u108f', u'\u1014', output) # na_nge
    output = re.sub(u'\u104e', u'\u104e\u1044\u103a\u1038', output) # le_gaung

# nga_sint

    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u108b', u'\u1064\\1\u102d', output)
    output = re.sub(u'([\u1000-\u1021])\u108c', u'\u1064\\1\u102e', output)
    output = re.sub(u'([\u1000-\u1021])\u108d', u'\u1064\\1\u1036', output)
    output = re.sub(u'\u1064', u'\u1004\u103a\u1039', output)
    output = re.sub(u'\u108e', u'\u102d\u1036', output)

    output = re.sub(u'\u105a', u'\u102b\u102c', output) # yaychar_hathtoe
    output = re.sub(u'\u1088', u'\u103e\u102f', output) # hahtoe_and_ta_chaung_ngin
    output = re.sub(u'\u1089', u'\u103e\u1030', output) # hahtoe_and_na_chaung_ngin
    output = re.sub(u'\u108a', u'\u103d\u103e', output) # wa_swal

    

    return output
