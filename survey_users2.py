import MySQLdb
import random
from config import *

def main():

	wikis = ['ru', 'pt', 'fr', 'ja', 'de', 'it', 'nl', 'pl']
	# wikis = ['test']
	f1 = open( 'survey_users2.txt', 'w' )

	for wiki in wikis:
		db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		res = query( wiki, db )
		res = random.sample( res, 500 )
		f1.write( '------------' +  wiki + '------------\n' )
		for r in res:
			f1.write( r + '\n' )
		f1.write( '\n\n' )


def query( wiki, db ):
	# [main, file, template, module, project, category, portal]
	namespaces = [ [0, 6, 10, 828, 4, 14, 100] ]
	cur = db.cursor()

	list1 = set()

	for n in namespaces:
		placeholders = ','.join( ['%s'] * len(n) )

		q = """SELECT rc_user, rc_user_text, SUM(CASE WHEN rc_namespace IN (%s) THEN 1 ELSE 0 END) AS hits
			   FROM recentchanges
			   WHERE rc_bot = 0
			   AND rc_user != 0
			   AND rc_user NOT IN ( SELECT DISTINCT ug_user FROM user_groups WHERE ug_group = 'bot' )
			   GROUP by rc_user_text
			   ORDER BY hits DESC
			   LIMIT 500;
			"""
		cur.execute( q % placeholders, tuple(n) )

		for row in cur.fetchall():
			list1.add( row[1] )

	print len(list1)
	return list1



main()




