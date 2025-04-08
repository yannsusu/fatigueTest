import serial
import time
import mysql.connector
import time

#mysql config
mysql_config = {
    'host':'192.168.137.203',
    'database':'fatigueTest',
    'user':'root',
    'password':'tansome'
}

def clear_table(cursor):
    select_query = 'SELECT *FROM Microbit ORDER BY time DESC LIMIT 10'
    cursor.execute(select_query)
    latest_data = cursor.fetchall()
    cursor.execute('TRUNCATE TABLE Microbit')
    insert_query = 'INSERT INTO Microbit (time, vepov, tozut) VALUES (%s, %s, %s)'
    for data in latest_data:
        cursor.execute(insert_query, data)
        
def add_data(cursor, time_value, vepov_value, tozut_value):
    insert_query = 'INSERT INTO Microbit (time, vepov, tozut) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (time_value, vepov_value, tozut_value))
    
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

clear_table(cursor)

def sendCommand(command):
		
	command = command + '\n'
	ser.write(str.encode(command))



def waitResponse():
	
	response = ser.readline()
	response = response.decode('utf-8').strip()
	
	return response


try:

	print("Listening on /dev/ttyACM0... Press CTRL+C to exit")	
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
	
	# Handshaking
	sendCommand('handshake')
	
	strMicrobitDevices = ''
	
	while strMicrobitDevices == None or len(strMicrobitDevices) <= 0:
		
		strMicrobitDevices = waitResponse()
		time.sleep(0.1)
	
	strMicrobitDevices = strMicrobitDevices.split('=')
	
	if len(strMicrobitDevices[1]) > 0:        
		
		listMicrobitDevices = strMicrobitDevices[1].split(',')
		
		if len(listMicrobitDevices) > 0:
				
			for mb in listMicrobitDevices:
				
				print('Connected to micro:bit device {}...'.format(mb))
			
			while True:
				
				#txCommand = input('Do you want to transmit command to micro:bit (y/n) = ')
				#if txCommand == 'y':
				commandToTx = 'sensor=acc'
				sendCommand('cmd:'+ commandToTx)
				print('Finished sending command to all micro:bit devices...')
					
				if commandToTx.startswith('sensor='):
					
					strSensorValues = ''
						
					while strSensorValues == None or len(strSensorValues) <= 0:
							
						strSensorValues = waitResponse()
						time.sleep(0.1)
						
					listSensorValues = strSensorValues.split(',')
						
					for sensorValue in listSensorValues:
						
						print(sensorValue)
						vepov = sensorValue
					
				time.sleep(0.1)
				commandToTx1 = 'sensor=temp'
				sendCommand('cmd:'+ commandToTx1)
				print('Finished sending command to all micro:bit devices...')
					
				if commandToTx1.startswith('sensor='):
					
					strSensorValues = ''
						
					while strSensorValues == None or len(strSensorValues) <= 0:
							
						strSensorValues = waitResponse()
						time.sleep(0.1)
						
					listSensorValues = strSensorValues.split(',')
						
					for sensorValue in listSensorValues:
						
						print(sensorValue)
						tozut = sensorValue
					
				time.sleep(0.1)
				current_time = time.time()
				add_data(cursor,current_time,vepov,tozut)
				connection.commit()
	
except KeyboardInterrupt:

	if ser.is_open:
		ser.close()
	
	print("Program terminated!")
