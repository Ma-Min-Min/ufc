# -*- coding: utf-8 -*-
import unittest
import zg2uni
import uni2win

class TestZG2WIN(unittest.TestCase):
   def test_article_one(self):
        zawgyi = u'''အပိုဒ္ ၁
        လူတိုင္းသည္ တူညီ လြတ္လပ္ေသာ ဂုဏ္သိကၡာျဖင့္ လည္းေကာင္း၊ တူညီလြတ္လပ္ေသာ အခြင့္အေရးမ်ားျဖင့္ လည္းေကာင္း၊ ေမြးဖြားလာသူမ်ား ျဖစ္သည္။ 
        ထိုသူတို႔၌ ပိုင္းျခား ေဝဖန္တတ္ေသာ ဉာဏ္ႏွင့္ က်င့္ဝတ္ သိတတ္ေသာ စိတ္တို႔ရွိၾက၍ ထိုသူတို႔သည္ အခ်င္းခ်င္း ေမတၱာထား၍ ဆက္ဆံက်င့္သုံးသင့္၏။'''
        win = u'''tydk'f 1
        vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/ 
        xdkolwdkYü ydkif;jcm; a0zefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY&SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        result = zg2uni.convert(zawgyi)
        result = uni2win.convert(result)
        self.assertEqual(win, result, "Failed to Convert Article One")

    def test_article_two(self):
        zawgyi = u'''အပိုဒ္ ၂
        လူတိုင္းသည္ လူ႔အခြင့္ အေရး ေၾကညာစာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရး အားလုံး၊ လြတ္လပ္ခြင့္ အားလုံးတို႔ကို ပိုင္ဆိုင္ ခံစားခြင့္ရွိသည္။ 
        လူမ်ိဳးႏြယ္အားျဖင့္ ျဖစ္ေစ၊ အသားအေရာင္အားျဖင့္ ျဖစ္ေစ၊ က်ား၊ မ၊ သဘာဝအားျဖင့္ ျဖစ္ေစ၊ ဘာသာစကားအားျဖင့္ ျဖစ္ေစ၊ ကိုးကြယ္သည့္ ဘာသာအားျဖင့္ ျဖစ္ေစ၊ 
        ႏိုင္ငံေရးယူဆခ်က္၊ သို႔တည္းမဟုတ္ အျခားယူဆခ်က္အားျဖင့္ ျဖစ္ေစ၊ ႏိုင္ငံႏွင့္ ဆိုင္ေသာ၊ သို႔တည္းမဟုတ္ လူမႈအဆင့္အတန္းႏွင့္ ဆိုင္ေသာ ဇစ္ျမစ္ အားျဖင့္ျဖစ္ေစ၊ 
        ပစၥည္း ဥစၥာ ဂုဏ္အားျဖင့္ ျဖစ္ေစ၊ မ်ိဳး႐ိုးဇာတိအားျဖင့္ ျဖစ္ေစ၊ အျခား အဆင့္အတန္း အားျဖင့္ ျဖစ္ေစ ခြဲျခားျခင္းမရွိေစရ။ ထို႔ျပင္ လူတစ္ဦး တစ္ေယာက္ 
        ေနထိုင္ရာ ႏိုင္ငံ၏ သို႔တည္းမဟုတ္ နယ္ေျမေဒသ၏ ႏိုင္ငံေရးဆိုင္ရာ ျဖစ္ေစ စီရင္ပိုင္ခြင့္ဆိုင္ရာ ျဖစ္ေစ တိုင္းျပည္ အခ်င္းခ်င္း ဆိုင္ရာျဖစ္ေစ၊ အဆင့္အတန္း တစ္ခုခုကို 
        အေျချပဳ၍ ေသာ္လည္းေကာင္း၊ ေဒသနယ္ေျမတစ္ခုသည္ အခ်ဳပ္အျခာ အာဏာပိုင္ လြတ္လပ္သည့္ နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကုလသမဂၢ ထိန္းသိမ္း ေစာင့္ေရွာက္ ထားရသည့္ 
        နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကိုယ္ပိုင္ အုပ္ခ်ဳပ္ခြင့္ အာဏာတို႔ တစိတ္တေဒသေလာက္သာ ရရွိသည့္ နယ္ေျမ စသျဖင့္ ယင္းသို႔ ေသာ နယ္ေျမမ်ား ျဖစ္သည္ 
        ဟူေသာ အေၾကာင္းကို အေထာက္အထား ျပဳ၍ ေသာ္လည္းေကာင္း ခြဲျခားျခင္း လုံးဝ မရွိေစရ။'''
        win = u'''tydk'f 2
        vlwdkif;onf vlYtcGihf ta&; aMunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkYudk ydkifqdkif cHpm;cGihf&Sdonf/ 
        vlrsdK;EG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap? 
        EdkifiHa&;,lqcsuf? odkYwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? EdkifiHESihf qdkifaom? odkYwnf;r[kwf vlrItqihftwef;ESihf qdkifaom Zpfjrpf tm;jzihfjzpfap? 
        ypönf; Opöm *kPftm;jzihf jzpfap? rsdK;½dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r&Sdap&/ xdkYjyif vlwpfOD; wpfa,muf 
        aexdkif&m EdkifiH\ odkYwnf;r[kwf e,fajra'o\ EdkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap wdkif;jynf tcsif;csif; qdkif&mjzpfap? tqihftwef; wpfckckudk 
        tajcûyí aomfvnf;aumif;? a'oe,fajrwpfckonf tcsKyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkYwnf;r[kwf ukvor*¾ xdef;odrf; apmihfa&Smuf xm;&onhf 
        e,fajr? odkYwnf;r[kwf udk,fydkif tkyfcsKyfcGihf tmPmwdkY wpdwfwa'oavmufom &&Sdonhf e,fajr pojzihf ,if;odkY aom e,fajrrsm; jzpfonf 
        [laom taMumif;udk taxmuftxm; ûyí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r&Sdap&/'''
        result = zg2uni.convert(zawgyi)
        result = uni2win.convert(result)
        self.assertEqual(win, result, "Failed to Convert Article Two")


if __name__ == "__main__":
    unittest.main()

