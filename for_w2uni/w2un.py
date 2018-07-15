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
    
