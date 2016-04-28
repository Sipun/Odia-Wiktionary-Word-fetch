#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import check_output

i = 1
while i != 100000:
    art = open('C:\Users\Shitikantha\Desktop\ddd.txt')
    art = art.read()
    art = "\n" + "Download_Start:" + "\n\n" + art

    con = art.count('(ଦେଖ)')
    while con != 0:
        if "(ଦେଖ)" in art:
            sub_art = art.split("(ଦେଖ)", 1)
            sub_art = sub_art[0].rsplit("<or>", 1)
            sub_art_pre = "<or>" + sub_art[1] + "(ଦେଖ)"
            sub_art_pre = "".join(sub_art_pre.splitlines())
            if "</nmb>" not in sub_art_pre:
                sub_art = "<or>[[" + sub_art[1] + "]] (eଦେଖ) - "
            else:
                sub_art_chk = sub_art[1]
                sub_art = "<or>" + sub_art[1] + "]] (eଦେଖ) - "
                sub_art = sub_art.replace("</nmb>", "</nmb>[[")
                sub_art = sub_art.replace("  ", " ")
                sub_art = sub_art.replace("  ", " ")
                if "[[ ]]" in sub_art:
                    sub_art = sub_art_chk
                    sub_art = "<or>" + sub_art + " (eଦେଖ) - "
                    sub_art = sub_art.replace("<or>", "<or>[[")
                    sub_art = sub_art.replace("<nmb>", "]] <nmb>")

            sub_art = "".join(sub_art.splitlines())
            art = art.replace(sub_art_pre, sub_art)
            con-=1

    art = art.replace("(eଦେଖ)", "(ଦେଖ)")

    art = art.replace('ୟ','swap#1')
    art = art.replace('ଯ','ୟ')
    art = art.replace('swap#1','ଯ')
    art = art.replace('ର୍ବ','ର୍tବ')
    art = art.replace('୍ବ','୍ୱ')
    art = art.replace('ର୍tବ','ର୍ବ')

    pagename = art.split("<b>", 1)
    pagename = pagename[1].split('</b>', 1)
    pagename = pagename[0]
    ipa = "|"+ check_output(["espeak", "-q", "--ipa", '-v', 'or', pagename ], shell=True) + '}}'
    ipa = "".join(ipa.splitlines())

    art = art.replace('<gramgrp><p><or>','\n=== ')
    art = art.replace('</or>—</p>',' ===\n')
    art = art.replace('<p>','\n')
    art = art.replace('</p>','\n')

    if "<syn>" in art:
        art_or = art.split("<syn>", 1)
        art_or = art_or[1].split("</syn>", 1)
        art_or = art_or[0]
        if "<or>" in art_or:
            art_or_pre = "<syn>" + art_or + "</syn>"
            art_or = art_or.replace("<or>", "\n<or>* ")
            art_or = art_or.replace("</or>", "\n")
            art_or = "<syn>" + art_or + "</syn>"
            art = art.replace(art_or_pre, art_or)

    art = art.replace('<syn>','\n=== ଅନୁବାଦ ===\n{{trans-top|{{subst:PAGENAME}}}}\n')
    art = art.replace('</syn>','\n{{trans-bottom}}\n')

    if "<be>" in art:
        art_be = art.split("<be>", 1)
        art_be = art_be[1].split("</be>", 1)
        art_be = "<be>" + art_be[0] + "</be>"
        art_be2 = art_be.replace(",", ']], [[')
        art_be2 = art_be2.replace(";", ']], [[')
        art = art.replace(art_be , art_be2)
        
    if "<d>" in art:
        art_d = art.split("<d>", 1)
        art_d = art_d[1].split("</d>", 1)
        art_d = "<d>" + art_d[0] + "</d>"
        art_d2 = art_d.replace(",", ']], [[')
        art_d2 = art_d2.replace(";", ']], [[')
        art = art.replace(art_d , art_d2)
        
    art = art.replace('<be>','* ବଙ୍ଗାଳୀ: [[')
    art = art.replace('</be>',']]\n')
    art = art.replace('<d>','* ହିନ୍ଦୀ: [[')
    art = art.replace('</d>',']]\n')
    art = art.replace('</or>',' ')
    art = art.replace('<sense>','')
    art = art.replace('</sense>',' ')
    art = art.replace('<gramgrp>','')
    art = art.replace('</gramgrp>',' ')
    art = art.replace('</span>','')
    art = art.replace('<verse>','')
    art = art.replace('</verse>','')
    art = art.replace('<gender>','')
    art = art.replace('</gender>',' ')
    art = art.replace('<curly>',"''")
    art = art.replace('</curly>',"''")
    art = art.replace('<tr>',"\n=== ଉଚ୍ଚାରଣ ===\n{{ଉଚ୍ଚାରଣ|")
    art = art.replace('<center>','<!--')
    art = art.replace('</center>','-->')
    art = art.replace('<b>',"'''")
    art = art.replace('</b>',"'''")
    art = art.replace("''' (ଧାତୁ)"," (ଧାତୁ)'''")
    art = art.replace("''' (ଇତ୍ୟାଦି)"," (ଇତ୍ୟାଦି)'''")
    art = art.replace("'''—","'''\n== [[ଓଡ଼ିଆ]] ==\n")
    art = art.replace("''' —","'''\n== [[ଓଡ଼ିଆ]] ==\n")

    art = art.replace('<nmb>1</nmb>ମ','୧ମ')
    art = art.replace('<nmb>2</nmb>ୟ','୨ୟ')
    art = art.replace('<nmb>3</nmb>ୟ','୩ୟ')
    art = art.replace('<nmb>4</nmb>ର୍ଥ','୪ର୍ଥ')
    art = art.replace('<nmb>5</nmb>ମ','୫ମ')
    art = art.replace('<nmb>6</nmb>ଷ୍ଠ','୬ଷ୍ଠ')
    art = art.replace('<nmb>7</nmb>ମ','୭ମ')
    art = art.replace('<nmb>8</nmb>ମ','୮ମ')
    art = art.replace('<nmb>9</nmb>ମ','୯ମ')
    art = art.replace('<nmb>1</nmb>ଟା','୧ଟା')
    art = art.replace('<nmb>2</nmb>ଟା','୨ଟା')
    art = art.replace('<nmb>3</nmb>ଟା','୩ଟା')
    art = art.replace('<nmb>4</nmb>ଟା','୪ଟା')
    art = art.replace('<nmb>5</nmb>ଟା','୫ଟା')
    art = art.replace('<nmb>6</nmb>ଟା','୬ଟା')
    art = art.replace('<nmb>7</nmb>ଟା','୭ଟା')
    art = art.replace('<nmb>8</nmb>ଟା','୮ଟା')
    art = art.replace('<nmb>9</nmb>ଟା','୯ଟା')
    art = art.replace('<nmb>0</nmb>ଟା','୦ଟା')
    art = art.replace('</nmb>ଶ','ଶ')
    art = art.replace('</nmb>ତମ','ତମ')
    art = art.replace('<p><nmb>',':<p><nmb>')
    art = art.replace('<or><nmb>1</nmb>',':୧. ')
    art = art.replace('<or><nmb>2</nmb>',':୨. ')
    art = art.replace('<or><nmb>3</nmb>',':୩. ')
    art = art.replace('<or><nmb>4</nmb>',':୪. ')
    art = art.replace('<or><nmb>5</nmb>',':୫. ')
    art = art.replace('<or><nmb>6</nmb>',':୬. ')
    art = art.replace('<or><nmb>7</nmb>',':୭. ')
    art = art.replace('<or><nmb>8</nmb>',':୮. ')
    art = art.replace('<or><nmb>9</nmb>',':୯. ')
    art = art.replace('<or><nmb>0</nmb>',':୦. ')
    art = art.replace('<or><nmb>10</nmb>',':୧୦. ')
    art = art.replace('<or><nmb>11</nmb>',':୧୧. ')
    art = art.replace('<or><nmb>12</nmb>',':୧୨. ')
    art = art.replace('<or><nmb>13</nmb>',':୧୩. ')
    art = art.replace('<or><nmb>14</nmb>',':୧୪. ')
    art = art.replace('<or><nmb>15</nmb>',':୧୫. ')
    art = art.replace('<or><nmb>16</nmb>',':୧୬. ')
    art = art.replace('<or><nmb>17</nmb>',':୧୭. ')
    art = art.replace('<or><nmb>18</nmb>',':୧୮. ')
    art = art.replace('<or><nmb>19</nmb>',':୧୯. ')
    art = art.replace('<or><nmb>20</nmb>',':୨୦. ')
    art = art.replace('<or><nmb>21</nmb>',':୨୧. ')
    art = art.replace('<or><nmb>22</nmb>',':୨୨. ')
    art = art.replace('<or><nmb>23</nmb>',':୨୩. ')
    art = art.replace('<or><nmb>24</nmb>',':୨୪. ')
    art = art.replace('<or><nmb>25</nmb>',':୨୫. ')
    art = art.replace('<or><nmb>26</nmb>',':୨୬. ')
    art = art.replace('<or><nmb>27</nmb>',':୨୭. ')
    art = art.replace('<or><nmb>28</nmb>',':୨୮. ')
    art = art.replace('<or><nmb>29</nmb>',':୨୯. ')
    art = art.replace('<or><nmb>30</nmb>',':୩୦. ')
    art = art.replace('<or><nmb>31</nmb>',':୩୧. ')
    art = art.replace('<or><nmb>32</nmb>',':୩୨. ')
    art = art.replace('<or><nmb>33</nmb>',':୩୩. ')
    art = art.replace('<or><nmb>34</nmb>',':୩୪. ')
    art = art.replace('<or><nmb>35</nmb>',':୩୫. ')
    art = art.replace('<or><nmb>36</nmb>',':୩୬. ')
    art = art.replace('<or><nmb>37</nmb>',':୩୭. ')
    art = art.replace('<or><nmb>38</nmb>',':୩୮. ')
    art = art.replace('<or><nmb>39</nmb>',':୩୯. ')
    art = art.replace('<or><nmb>40</nmb>',':୪୦. ')
    art = art.replace('<or>','')
    art = art.replace('<nmb>1</nmb>','୧')
    art = art.replace('<nmb>2</nmb>','୨')
    art = art.replace('<nmb>3</nmb>','୩')
    art = art.replace('<nmb>4</nmb>','୪')
    art = art.replace('<nmb>5</nmb>','୫')
    art = art.replace('<nmb>6</nmb>','୬')
    art = art.replace('<nmb>7</nmb>','୭')
    art = art.replace('<nmb>8</nmb>','୮')
    art = art.replace('<nmb>9</nmb>','୯')
    art = art.replace('<nmb>0</nmb>','୦')
    art = art.replace('1','୧')
    art = art.replace('2','୨')
    art = art.replace('3','୩')
    art = art.replace('4','୪')
    art = art.replace('5','୫')
    art = art.replace('6','୬')
    art = art.replace('7','୭')
    art = art.replace('8','୮')
    art = art.replace('9','୯')
    art = art.replace('0','୦')
    art = art.replace('<nmb>','')
    art = art.replace('</nmb>',': ')

    art = art.replace(' * ହିନ୍ଦୀ:','* ହିନ୍ଦୀ:')
    art = art.replace(' * ବଙ୍ଗାଳୀ:','* ବଙ୍ଗାଳୀ:')

    art = art.replace(' ପୁଂ ','ପୁଲିଙ୍ଗ - ')
    art = art.replace(' ସଂ ','ସଂସ୍କୃତ - ')
    art = art.replace(' ଗ୍ରା ','ଗ୍ରାମ୍ୟ - ')
    art = art.replace(' ଦେ ','ଦେଶଜ - ')
    art = art.replace(' ବିଣ ','ବିଶେଷଣ - ')
    art = art.replace(' ବୈଦେ ','ବୈଦେଶିକ - ')
    art = art.replace('ତୁଳ—','ତୁଳନା - ')
    art = art.replace('[ଦ୍ର',"['''ଦ୍ରଷ୍ଟବ୍ୟ''' ")
    art = art.replace('<gramgrp>','')
    art = art.replace(' ବି ',' ବିଶେଷ୍ୟ - ')
    art = art.replace(' କ୍ରି ','କ୍ରିୟାପଦ - ')
    art = art.replace(' ପ୍ରାଦେ ','ପ୍ରାଦେଶିକ - ')
    art = art.replace('ପ୍ରାଦେ.','ପ୍ରାଦେଶିକ - ')
    art = art.replace('ବୈଦେ.','ବୈଦେଶିକ - ')
    art = art.replace('ଦେ.','ଦେଶଜ - ')
    art = art.replace('ସଂ.','ସଂସ୍କୃତ - ')
    art = art.replace('ଗ୍ରା.','ଗ୍ରାମ୍ୟ - ')
    art = art.replace('ବିଣ.','ବିଶେଷଣ - ')
    art = art.replace('ବି.','ବିଶେଷ୍ୟ - ')
    art = art.replace('ଆ.','ଆରବୀ - ')
    art = art.replace('ଇଂ.','ଇଂରାଜୀ - ')
    art = art.replace('ହି.','ହିନ୍ଦୀ - ')
    art = art.replace('ଫା.','ଫାରାସୀ - ')
    art = art.replace('ବଂ.','ବଙ୍ଗାଳୀ - ')
    art = art.replace('ତେ.','ତେଲୁଗୁ - ')
    art = art.replace('</tr>',ipa)
    art = art.replace('<br/>','\n')
    art = art.replace("- —", "-")
    art = art.replace("  ", " ")
    art = art.replace("  ", " ")
    
    if "[[]]" in art:
        art = art + "\n[[ଶ୍ରେଣୀ:need check]]\n"

    art = art +  "\n------------------\n" + "[[ଶ୍ରେଣୀ:ବଟ ତିଆରି ୩]]" + "\n\n" + "Download_End" + "\n\n"
    print art
    print i
    i+=1
