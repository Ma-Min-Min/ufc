# -*- coding: utf-8 -*-

import re

def replace(input)
    
    output = input
    
    
    output = re.sub(u'\u0075', u'\u1000', output) # ka_gyi
    output = re.sub(u'\u0063', u'\u1001', output) # kha_kway
    output = re.sub(u'\u002a', u'\u1002', output) # ga_nge
    output = re.sub(u'\u0043', u'\u1003', output) # ga_gyi
    output = re.sub(u'\u0069', u'\u1004', output) # nga
    output = re.sub(u'\u0070', u'\u1005', output) # sa_lone
    output = re.sub(u'\u0071', u'\u1006', output) # sa_lane
    output = re.sub(u'\u005a', u'\u1007', output) # za_gwal
    output = re.sub(u'\u00da', u'\u1009', output) # nya_pyat
    output = re.sub(u'[\u006e\u00d1]', u'\u100a', output) # nya
    output = re.sub(u'\u0023', u'\u100b', output) # ta_taling_chake
    output = re.sub(u'\u0058', u'\u100c', output) # hta_win_bae
    output = re.sub(u'\u0021', u'\u100d', output) # da_yin_cout
    output = re.sub(u'\u00a1', u'\u100e', output) # da_yay_mote
    output = re.sub(u'\u0050', u'\u100f', output) # na_gyi
    output = re.sub(u'\u0077', u'\u1010', output) # ta_win_pu
    output = re.sub(u'\u0078', u'\u1011', output) # hta_sin_htoo
    output = re.sub(u'\u0027', u'\u1012', output) # da_dwe
    output = re.sub(u'\u0022', u'\u1013', output) # da_out_chai
    output = re.sub(u'[\u0045\u0065]', u'\u1014', output) # na_nge
    output = re.sub(u'\u0079', u'\u1015', output) # pa_thout
    output = re.sub(u'\u007a', u'\u1016', output) # pha_oo_htoke
    output = re.sub(u'\u0041', u'\u1017', output) # ba_htet_chai
    output = re.sub(u'\u0062', u'\u1018', output) # ba_gone
    output = re.sub(u'\u0072', u'\u1019', output) # ma
    output = re.sub(u'\u002c', u'\u101a', output)# ya_pa_lat
    output = re.sub(u'[\u0026\u00bd]', u'\u101b', output)  # ya_gout
    output = re.sub(u'\u0076', u'\u101c', output)  # la
    output = re.sub(u'\u0030', u'\u101d', output)  # wa
    output = re.sub(u'\u006f', u'\u101e', output)  # tha
    output = re.sub(u'\u005b', u'\u101f', output)  # ha
    output = re.sub(u'\u0056', u'\u1020', output)  # la_gyi
    output = re.sub(u'\u0074', u'\u1021', output)  # aa

    output = re.sub(u'\u00fe', u'\u1024', output) # ai
    output = re.sub(u'[\u004f\u00cd]', u'\u1025', output)  # au
    output = re.sub(u'\u007b', u'\u1027', output) # at_kayar_au
    output = re.sub(u'\u0067', u'\u102b', output) # mout_cha
    output = re.sub(u'\u006d', u'\u102c', output) # wide_cha
    output = re.sub(u'\u0064', u'\u102d', output) # lone_gyi_tin
    output = re.sub(u'\u0044', u'\u102e', output) # lone_gyi_tin_sankat
    output = re.sub(u'\u1025\u102e', u'\u1026', output) # lone_gyi_tin_sankat_oo
    output = re.sub(u'[\u004b\u006b]', u'\u102f', output) # ta_chaung_ngin
    output = re.sub(u'[\u004c\u006c]', u'\u1030', output) # na_chaung_ngin
    output = re.sub(u'\u0061', u'\u1031', output) # tha_wai_htoe
    output = re.sub(u'\u004a', u'\u1032', output) # nout_htoe_pyit
    output = re.sub(u'\u0048', u'\u1036', output) # taytay_tin
    output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output) # out_myit
    output = re.sub(u'\u003b', u'\u1038', output) # wa_sa_pout
    output = re.sub(u'\u0066', u'\u103a', output) # nga_tat
    output = re.sub(u'[\u0073\u00df]', u'\u103b', output) # ya_pint
    output = re.sub(u'\u1005\u103b', u'\u1008', output) # za_myit_zwe
    output = re.sub(u'[\u006A\u0042\u004d\u004e\u0060\u007e]', u'\u103c', output) # ya_yit
    output = re.sub(u'\u0047', u'\u103d', output) # wa_swe
    output = re.sub(u'[\u0053\u00a7]', u'\u103e', output) # ha_toe
    output = re.sub(u'\u00f3', u'\u003f', output) # ta_gyi
