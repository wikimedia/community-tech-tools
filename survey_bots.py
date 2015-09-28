import MySQLdb
import random
from config import *

def main():

	wikis = ['ar', 'ru', 'en', 'fr', 'ja', 'de', 'commons', 'es', 'zh', 'pt']
	f1 = open( 'survey_bots.txt', 'w' )
	
	for wiki in wikis:
		db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		query( wiki, db, f1 )
		# f1.write( wiki + '\t' + str( len( res ) ) + '\n' )
		# for r in res:
		# 	if r is not None:
		# 		f1.write( r + '\t' + res[r] + '\n' )
		# 	else:
		# 		f1.write( 'None \t This user is None! \n ')
		# f1.write( '\n\n' )


def query( wiki, db, f1 ):
	cur = db.cursor()
	list1 = {}
	q = """SELECT rc_user, rc_user_text, COUNT(*) AS edits
		   FROM recentchanges
		   WHERE rc_bot = 1
		   GROUP by rc_user
		   ORDER BY edits DESC
		   LIMIT 100
		"""
	cur.execute(q)

	for row in cur.fetchall():
		list1[str(row[1])] = str(row[2])

	print len( list1 )
	if len( list1 ) > 25:
		keys = random.sample( list1, 25 )
		values = [list1[k] for k in keys]
	else:
		keys = [x for x in list1]
		values = [list1[x] for x in keys]
	f1.write( wiki + '\t' + str(len(keys)) + '\n' )
	for i in range(0, len(keys)):
		f1.write( str(keys[i]) + '\t\t' + str(values[i]) + '\n')
	f1.write( '\n\n\n' )

main()
