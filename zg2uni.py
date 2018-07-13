# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input

    output = output.replace(u'\u106a', u'\u1009')  # nya_lay
    output = re.sub(u'\u106b', u'\u100a', output)  # nya
    output = re.sub(u'\u1090', u'\u101b', output)  # ya_guat
    output = re.sub(u'\u1033', u'\u102f', output)  # ta_chuang_ngin
    output = re.sub(u'\u1034', u'\u1030', output)  # na_chuang_ngin
    output = re.sub(u'[\u103d\u1087]', u'\u103e', output)  # ha_toe
    output = re.sub(u'\u103c', u'\u103d', output)  # wa_swe
    output = re.sub(u'\u1086', u'\u103f', output)  # ta_gyi
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output)  # ya_yit
    output = re.sub(u'[\u103a\u107d]', u'\u103b', output)  # ya_pint
    output = re.sub(u'\u1039', u'\u103a', output)  # nga_tat
    output = re.sub(u'\u104e', u'\u104e\u1044\u103a\u1038', output)  # la_guang
    output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037', output)  # aut_myit
    output = re.sub(u'\u108f', u'\u1014', output)  # na_nge

    # nga_sint

    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u108b', u'\u1064\\1\u102d', output)
    output = re.sub(u'([\u1000-\u1021])\u108c', u'\u1064\\1\u102e', output)
    output = re.sub(u'([\u1000-\u1021])\u108d', u'\u1064\\1\u1036', output)
    output = re.sub(u'\u1064', u'\u1004\u103a\u1039', output)
    output = re.sub(u'\u108e', u'\u102d\u1036', output)


    output = re.sub(u'\u1088', u'\u103e\u102f', output)  # hahtoe_and_ta_chaung_ngin
    output = re.sub(u'\u1089', u'\u103e\u1030', output)  # hahtoe_and_na_chaung_ngin
    output = re.sub(u'\u105a', u'\u102b\u102c', output)  # yaychar_hathtoe
    output = re.sub(u'\u108a', u'\u103d\u103e', output)  # wa_swal

    # pat_sint

    output = re.sub(u'\u1060', u'\u1039\u1000', output)  # ka_gyi
    output = re.sub(u'\u1061', u'\u1039\u1001', output)  # kha_kway
    output = re.sub(u'\u1062', u'\u1039\u1002', output)  # ga_nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output)  # ga_gyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output)  # sa_lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output)  # sa_lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output)  # za_gwe
    output = re.sub(u'\u1069', u'\u1039\u1008', output)  # za_myin_zwe
    output = re.sub(u'\u106c', u'\u1039\u100b', output)  # ta_da_lin_jake
    output = re.sub(u'\u106d', u'\u1039\u100c', output)  # hta_wen_bae
    output = re.sub(u'\u106e', u'\u100d\u1039\u100d', output)  # da_yin_guat
    output = re.sub(u'\u106f', u'\u100d\u1039\u100e', output)  # da_yin_mot
    output = re.sub(u'\u1070', u'\u1039\u100f', output)  # na_gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output)  # ta_wen_pu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)  # hta_sin_htoo
    output = re.sub(u'\u1075', u'\u1039\u1012', output)  # da_dway
    output = re.sub(u'\u1076', u'\u1039\u1013', output)  # da_out_chai
    output = re.sub(u'\u1077', u'\u1039\u1014', output)  # nga_nge
    output = re.sub(u'\u1078', u'\u1039\u1015', output)  # pa_saut
    output = re.sub(u'\u1079', u'\u1039\u1016', output)  # pa_oo_htoke
    output = re.sub(u'\u107a', u'\u1039\u1017', output)  # ba_htet_chai
    output = re.sub(u'[\u107b\u1093]', u'\u1039\u1018', output)  # ba_gone
    output = re.sub(u'\u107c', u'\u1039\u1019', output)  # ma
    output = re.sub(u'\u1085', u'\u1039\u101c', output)  # la
    output = re.sub(u'\u1091', u'\u100f\u1039\u100d', output)  # na_gyi_and_da_yin_guat
    output = re.sub(u'\u1092', u'\u100b\u1039\u100c', output)  # ddlg&twb
    output = re.sub(u'\u1097', u'\u100b\u1039\u100b', output)  # twiceddlg

    return output


def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input
    ## 1=tawaetoe 2=yayit 3=letter 4=yapint 5=waswe 6=hatoe 7=aumyit 8=yaychar
    output = re.sub(
        u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)',
        '\\3\\2\\4\\5\\6\\1\\7\\8', output)
    ## for ta/na_chuangngin and longgyitin(sanke)
    output = re.sub(u'(\u102f)([\u102d\u102e])', '\\2\\1', output)
    output = re.sub(u'(\u1030)([\u102d\u102e])', '\\2\\1', output)

    return output
