import os

print('Make sure you are running this in administrator mode')

#these lists will be used instead of single variables

run_list = [' run ',' open ',' execute ',' open ',' execute ',' show ']
neg_list = [' dont ',' dont ','do not ',' not ',' not ',' not ']
exitc = [' exit ',' quit ',' stop ',' leave ',' leave ',' stop ']

#here we fill file_list with program names

try:
	f = open("program names","r")
	file_list = f.readlines()
	i = 0
	while i<len(file_list):
	    file_list[i] = file_list[i].replace('\n','')
	    file_list[i] = ' '+file_list[i]+' '
	    i += 1
	f.close()
except:
	print('File not found. Make sure you have the file "program names" in same folder in which you have 1.py')
#here we fill cmds with their respective commands

try:
	f1 = open("cmd names","r")
	cmds = f1.readlines()
	i = 0
	while i<len(cmds):
	    cmds[i] = cmds[i].replace('\n','')
	    cmds[i] = ' '+cmds[i]+' '
	    i += 1
	f1.close()
except:
	print('File not found. Make sure you have the file "cmd names" in same folder in which you have 1.py')

while True:

	print('Enter your choice : ', end = '')
	ans = ' '+input().lower()+' '
	neg = False
	run = True
	i = 0 
	brk = False
	file = False

#check if input contains any word from the exitc list 

	while i<len(exitc):		
		if exitc[i] in ans:			
			exit()	
		i = i + 1    

#check if string contains any word from neg list. i.e we dont run that command & set neg variable

	i = 0
	while i<len(neg_list):		
		if neg_list[i] in ans:
			neg = True
			break
		else:
			neg = False			
		i = i + 1

#check if input contains any word from the run list & set run variable

	i = 0
	while i<len(run_list):		
		if (run_list[i] in ans):	
			run = True
			break			
		else:	
			run = False			
		i = i + 1

#if we get a run var as True & neg as False(i.e we have to run some command). so we furthur check which program to run

	if run and not neg:

#check if input contains any word from the file list, run that program & set file variable

		i = 0
		while i<len(file_list):	
			if file_list[i] in ans:
				cmd = cmds[i]				
				os.system(cmd)
				file = True
				break	
			else:
				file = False		
			i = i + 1
	else:
		print("Something went wrong")

#if we dont find the file then we must add it 

	if not file:
		print('If you entered correctly still program did not work there is a chance it is not in our list.')
		print('Press a to add the program to our list.')
		to_add = input()
		if (to_add is 'a'):
			print('Enter program name')
			name = input().lower()
		
#add program name to file
			f1 = open("program names","a")
			f1.write("\n")
			f1.write(name)
			f1.close() 			
			print('Enter cmd for that program')
			command = input().lower()

#add cmd to file
			f1 = open("cmd names","a")
			f1.write("\n")
			f1.write(command)
			f1.close() 	
			print('Enter program path. Pls note it must be path where your program is installed')
			path = input().lower()

#add the address to the Path variable of their system using "setx command"
			os.system('setx path "%path%;'+path+'" /M')
			print('If there\'s a message saying ---truncated to 1204--- then you have to set the path manually through settings.') 
			print('The application must be restarted. Quitting application')
			exit()