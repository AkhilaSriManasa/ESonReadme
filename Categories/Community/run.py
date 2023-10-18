fp = open('listLanguages.txt','r')
ids = []
for id in fp:
    ids.append(id.replace("\n",""))
fp.close()

fp3 = open('lang.sh','a')
print(len(ids))

for x in ids:
    fp2 = open("script_"+x+".sh","a")
    fp2.write("python3 fishers.py "+x+"\n")
    # fp2.write("python3 Wilcoxon_test.py "+x+"\n")
    fp2.write("python3 spearman.py "+x+"\n")
    fp2.write("python3 id_corr_categories.py "+x+"\n")
    fp2.write("python3 rfc.py "+x+"\n")
    fp2.close()
    fp3.write("./script_"+x+".sh\n")


fp3.close()
