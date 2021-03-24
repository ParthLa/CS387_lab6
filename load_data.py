import csv
# CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
# run
# CREATE (hi:Hashtag {id:row[0], tag:row[1]})
# CREATE (ti:Tweet {id:row[0], text:row[1]})
# CREATE (ui:User {id:row[0], name:row[1]})
# MATCH (p1: Tweet{id:row[0]}), (p2: Hashtag{id:row[1]}) CREATE (p1)-[:Contains]->(p2);
# MATCH (p1: User{id:row[0]}), (p2: User{id:row[1]}) CREATE (p1)-[:Follows]->(p2);
# MATCH (p1: Tweet{id:row[0]}), (p2: User{id:row[1]}) CREATE (p1)-[:Mentions]->(p2);
# MATCH (p1: User{id:row[0]}), (p2: Tweet{id:row[1]}) CREATE (p1)-[:Sent]->(p2);

# CREATE (hi:Hashtag {id:row[0], tag:row[1]})
# CREATE (ti:Tweet {id:row[0], text:row[1]})
# CREATE (ui:User {id:row[0], name:row[1]})
# CREATE (h[row[0]])-[:Contains]->(t[row[1]])
# CREATE (u[row[0]])-[:Follows]->(u[row[1]])
# CREATE (t[row[0]])-[:Mentions]->(u[row[1]])
# CREATE (u[row[0]])-[:Sent]->(t[row[1]])

data_dir = "data/data/"

node_files = ["hashtags.csv","tweets.csv","users.csv"]
relation_files = ["contains.csv","follows.csv","mentions.csv","sent.csv"]

write_file = "cmds"
fw = open(write_file,'w')

path = data_dir + node_files[0]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (h"
	# stmt3 = ":Hashtag {id:"
	# stmt5 = ", tag: '"
	stmt7 = "})\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[0] + stmt5 + row[1] + stmt7
			stmt = 'CREATE (h%s:Hashtag {id:%s, tag:"%s"' %(row[0],row[0],row[1])
			stmt = stmt+stmt7
			fw.write(stmt)
			# fw.write("CREATE (h%s:Hashtag {id: %s, tag: %d )".format(row[0],row[0],row[1]))
		line_count = line_count + 1

path = data_dir + node_files[1]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (t"
	# stmt3 = ":Tweet {id:"
	# stmt5 = ", text: '"
	stmt7 = "})\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[0] + stmt5 + row[1] + stmt7
			stmt = 'CREATE (t%s:Tweet {id:%s, text:"%s"' %(row[0],row[0],row[1])
			stmt = stmt+stmt7
			fw.write(stmt)
		line_count = line_count + 1

path = data_dir + node_files[2]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (u"
	# stmt3 = ":User {id:"
	# stmt5 = ", name: '"
	stmt7 = "})\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[0] + stmt5 + row[1] + stmt7
			stmt = 'CREATE (u%s:User {id:%s, name:"%s"' %(row[0],row[0],row[1])
			stmt = stmt+stmt7
			fw.write(stmt)
		line_count = line_count + 1

# CREATE (h[row[0]])-[:Contains]->(t[row[1]])
# CREATE (u[row[0]])-[:Follows]->(u[row[1]])
# CREATE (t[row[0]])-[:Mentions]->(u[row[1]])
# CREATE (u[row[0]])-[:Sent]->(t[row[1]])

path = data_dir + relation_files[0]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (t"
	# stmt3 = ")-[:Contains]->(h"
	# stmt5 = ")\n"
	# stmt7 = "'})\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[1] + stmt5
			stmt = 'CREATE (t%s)-[:Contains]->(h%s)\n' %(row[0],row[1])
			# stmt = stmt+stmt7
			fw.write(stmt)
		line_count = line_count + 1

path = data_dir + relation_files[1]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (u"
	# stmt3 = ")-[:Follows]->(u"
	# stmt5 = ")\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[1] + stmt5 
			stmt = 'CREATE (u%s)-[:Follows]->(u%s)\n' %(row[0],row[1])
			fw.write(stmt)
		line_count = line_count + 1

path = data_dir + relation_files[2]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (t"
	# stmt3 = ")-[:Mentions]->(u"
	# stmt5 = ")\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[1] + stmt5 
			stmt = 'CREATE (t%s)-[:Mentions]->(u%s)\n' %(row[0],row[1])
			fw.write(stmt)
		line_count = line_count + 1

path = data_dir + relation_files[3]
with open(path,'r') as f:
	csv_reader = csv.reader(f,delimiter=',')
	# stmt1 = "CREATE (u"
	# stmt3 = ")-[:Sent]->(t"
	# stmt5 = ")\n"
	line_count = 0
	for row in csv_reader:
		if(line_count!=0):
			# stmt = stmt1 + row[0] + stmt3 + row[1] + stmt5 
			stmt = 'CREATE (u%s)-[:Sent]->(t%s)\n' %(row[0],row[1])
			fw.write(stmt)
		line_count = line_count + 1
