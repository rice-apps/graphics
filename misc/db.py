# db.py
import sqlite3 as sql
from datetime import datetime

con = sql.connect('apply.db')#, detect_types=sql.PARSE_DECLTYPES) #check_same_thread=False
cur = con.cursor()
SPACE = " "

print "ID | NAME" + SPACE * 15 + " | EMAIL" + SPACE * 15 \
	+ " | YEAR" + SPACE * 4 + " | POSITION" + SPACE * 15 + " | BANS" + SPACE * 15 + " | SKILLS" + SPACE * 15 + " | COMMENTS" + SPACE * 15 + " | MINIS | DATE"

cur.execute("SELECT * FROM application")
for i in cur.fetchall():
	print (str(i[0]) + SPACE * 2)[:2] + " | ",
	print (str(i[1]) + SPACE * 18)[:18] + " | ",
	print (str(i[2]) + SPACE * 19)[:19] + " | ",
	print (str(i[3]) + SPACE * 7)[:7] + " | ",
	print (str(i[4]) + SPACE * 22)[:22] + " | ",
	print (str(i[5]) + SPACE * 18)[:18] + " | ",
	print (str(i[6]) + SPACE * 20)[:20] + " | ",
	print (str(i[7]) + SPACE * 22)[:22] + " | ",
	print (str(i[8]) + SPACE * 4)[:4] + " | ",
	print (str(i[9]) + SPACE * 14)[:14] + " | "

# 	1|Xilin Liu|xal1@rice.edu|senior|Developer||                    python|i lurve ra|yes|2015-01-30 05:55:53.127041
# 2|offline|application|freshman|||                    |||2015-01-30 06:11:50.843700
# 3|Shirley Jiang|xj2@rice.edu|sophomore|Developer|Wellbeing App; Petition App Schedule Planner|python, Java, C, HTML/CSS|||2015-01-30 13:08:48.399415
# 4|Shirley Jiang|xj2@rice.edu|sophomore|Developer|Wellbeing App; Petition App Schedule Planner|python, Java, C, HTML/CSS||yes|2015-01-30 13:10:49.755089
# 5|Gloria Kim|gloria.kim@rice.edu|sophomore|Designer|Schedule Planner||Currently I am more comfortable designing than developing, but I am taking COMP182 this semester and may potentially major in CS.|yes|2015-01-30 13:18:49.566674
# 6|Brian Lee|brianlee.jpg@gmail.com|junior|Developer Designer Project Manager||All of the above, python||yes|2015-01-30 14:02:14.207617
# 7|Yingchen Xu|yx26@rice.edu|freshman|Developer Designer||Python, Java|||2015-01-30 14:30:00.277631
# 8|Oliver Xu|ox1@rice.edu|freshman|Project Manager||HTML/CSS||yes|2015-01-30 16:39:25.997214
# 9|Yingchen Xu|yx26@rice.edu|freshman|Developer Designer||Python, Java|||2015-01-30 17:49:41.210363
# 10|Ethan Perez|ejp2@rice.edu|freshman|Developer||Python, C, HTML, CSS, JavaScript|I'm willing to put a lot of time and effort into Rice Apps, because I really love what y'all are doing.|yes|2015-01-30 17:52:32.436636
# 11|Kunal Shah|ks45@Rice.edu|freshman|Developer Designer||Python||yes|2015-01-30 17:55:08.055341
# 12|Roshni Kaushik|rsk8@rice.edu|sophomore|Developer||HTML/CSS
# Javascript
# PHP and some SQL
# Python (only what is in COMP 140/182, I have not done any web development with Python)||yes|2015-01-30 18:29:18.037953
# 13|Nuozhou Xu|nx1@rice.edu|freshman|Developer|Wellbeing App|Python||yes|2015-01-30 20:05:12.594804
# 14|Christopher Jardine|cmj5@rice.ed|junior|Developer||Java, Python, C, HTML/CSS||yes|2015-01-30 20:21:12.454732