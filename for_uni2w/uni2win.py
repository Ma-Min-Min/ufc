# -*- coding: utf-8 -*-

import re


def replace(input):
    output = input

    output = re.sub(u'\u1000', u'\u0075', output)  # ka_gyi
    output = re.sub(u'\u1001', u'\u0063', output)  # ka_kway
    output = re.sub(u'\u1002', u'\u002a', output)  # ga_nge
    output = re.sub(u'\u1003', u'\u0043', output)  # ga_gyi
    output = re.sub(u'\u1004', u'\u0069', output)  # nga
    output = re.sub(u'\u1005', u'\u0070', output)  # sa_lone
    output = re.sub(u'\u1006', u'\u0071', output)  # sa_lane
    output = re.sub(u'\u1007', u'\u005a', output)  # za_gwal
    output = re.sub(u'\u1009', u'\u00da', output)  # nya_shay
    output = re.sub(u'\u100a', u'\u006e', output)  # nya
    output = re.sub(u'\u100b', u'\u0023', output)  # tata_lin_gyake
    output = re.sub(u'\u100c', u'\u0058', output)  # hta_wen_bae
    output = re.sub(u'\u100d', u'\u0021', output)  # da_yin_guat
    output = re.sub(u'\u100e', u'\u00a1', output)  # da_yin_mot
    output = re.sub(u'\u100f', u'\u0050', output)  # na_gyi
    output = re.sub(u'\u1010', u'\u0077', output)  # ta_win_pu
    output = re.sub(u'\u1011', u'\u0078', output)  # hta_sin_h
    too
    output = re.sub(u'\u1012', u'\u0027', output)  # da_dway
    output = re.sub(u'\u1013', u'\u0022', output)  # da_out_chai
    output = re.sub(u'\u1014', u'\u0065', output)  # na_nge
    output = re.sub(u'\u1015', u'\u0079', output)  # pa_sout
    output = re.sub(u'\u1016', u'\u007a', output)  # pa_oo_htoke
    output = re.sub(u'\u1017', u'\u0041', output)  # ba_htet_chai
    output = re.sub(u'\u1018', u'\u0062', output)  # ba_gone
    output = re.sub(u'\u1019', u'\u0072', output)  # ma
    output = re.sub(u'\u101a', u'\u002c', output)  # ya_pa_lat
    output = re.sub(u'\u101b', u'\u0026', output)  # ya_gaut
    output = re.sub(u'\u101c', u'\u0076', output)  # la
    output = re.sub(u'\u101d', u'\u0030', output)  # wa
    output = re.sub(u'\u101e', u'\u006f', output)  # tha
    output = re.sub(u'\u101f', u'\u005b', output)  # ha
    output = re.sub(u'\u1020', u'\u0056', output)  # la_gyi
    output = re.sub(u'\u1021', u'\u0074', output)  # aa
    output = re.sub(u'\u1023', u'\u00a3', output)  # 2kagyi
    output = re.sub(u'\u1024', u'\u00fe', output)  # II
    output = re.sub(u'\u1025', u'\u004f', output)  # oo
    output = re.sub(u'\u1027', u'\u007b', output)  # at_kayar_aa
    output = re.sub(u'\u102b', u'\u0067', output)  # yaychar_ashay
    output = re.sub(u'\u102c', u'\u006d', output)  # yaychar
    output = re.sub(u'\u102d', u'\u0064', output)  # long_gyi_tin
    output = re.sub(u'\u102e', u'\u0044', output)  # long_gyi_tin_sanke
    output = re.sub(u'\u102f', u'\u004b', output)  # 1_chuang_ngin
    output = re.sub(u'\u1030', u'\u004c', output)  # 2_chuang_ngin
    output = re.sub(u'\u1031', u'\u0061', output)  # ta_wai_toe
    output = re.sub(u'\u1032', u'\u004a', output)  # naut_htoe_pyit
    output = re.sub(u'\u1036', u'\u0048', output)  # tay_tay_tin
    output = re.sub(u'\u1037', u'\u0068', output)  # aut_myit
    output = re.sub(u'\u1038', u'\u003b', output)  # wa_sa_paut
    output = re.sub(u'\u103a', u'\u0066', output)  # nga_tat
    output = re.sub(u'\u103b', u'\u0073', output)  # ya_pint
    output = re.sub(u'\u103c', u'\u006a', output)  # ya_yit
    output = re.sub(u'\u103d', u'\u0047', output)  # wa_swe
    output = re.sub(u'\u103e', u'\u0053', output)  # ha_toe
    output = re.sub(u'\u103f', u'\u00f3', output)  # ta_gyi
    output = re.sub(u'\u1040', u'\u0030', output)  # 0
    output = re.sub(u'\u1041', u'\u0031', output)  # 1
    output = re.sub(u'\u1042', u'\u0032', output)  # 2
    output = re.sub(u'\u1043', u'\u0033', output)  # 3
    output = re.sub(u'\u1044', u'\u0034', output)  # 4
    output = re.sub(u'\u1045', u'\u0035', output)  # 5
    output = re.sub(u'\u1046', u'\u0036', output)  # 6
    output = re.sub(u'\u1047', u'\u0037', output)  # 7
    output = re.sub(u'\u1048', u'\u0038', output)  # 8
    output = re.sub(u'\u1049', u'\u0039', output)  # 9
    output = re.sub(u'\u104a', u'\u003f', output)  # pot_kalay
    output = re.sub(u'\u104b', u'\u002f', output)  # pot_ma
    output = re.sub(u'\u104c', u'\u00fc', output)  # nai
    output = re.sub(u'\u104d', u'\u00ed', output)  # yue
    output = re.sub(u'\u104e', u'\u00a4', output)  # la_guang
    output = output.replace(u'\u104f', u'\u005c')  # at_kayar_e

    return output
