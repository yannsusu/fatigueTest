import time
from bluetooth import ble

import util



class MyGATTRequester(ble.GATTRequester):

	_callback = None
	
	
	
	def on_notification(self, handle, data):
		
		self._callback(data[0])
	
	
	
	def on_indication(self, handle, data):				
		
		if data != None and len(data) > 2:
		
			data = data[2:]
		
		self._callback(data.decode('utf-8'))
	
	
	
	def set_callback(self, callback):
	
		self._callback = callback



class BleUartDevice:

	address = ''
	gattRequester = None

	
	
	def __init__(self, address):
		
		self.address = address
	
	
	
	def connect(self):
		
		self.gattRequester = MyGATTRequester(self.address, False)
		self.gattRequester.connect(True, 'random')
		time.sleep(1)
	
	
	
	def readTemperature(self):
		
		temp = self.gattRequester.read_by_handle(0x27)			
		temp = util.convertMicrobitValue(temp)
		return temp
	
	
	
	def enable_temperature_receive(self, callback):
	
		self.gattRequester.set_callback(callback)
		self.gattRequester.write_by_handle(0x28, '\x01\x00')
	
	
	
	def disable_temperature_receive(self):
		
		self.gattRequester.write_by_handle(0x28, '\x00\x00')
	
	
	
	def send(self, strData):
	
		txData = util.marshalStringForBleUartSending(strData)
		self.gattRequester.write_by_handle(0x2a, txData)
		time.sleep(1)
	
	
	
	def enable_uart_receive(self, callback):
	
		self.gattRequester.set_callback(callback)
		self.gattRequester.write_by_handle(0x28, '\x02\x00')
	
	def disable_uart_receive(self, callback):
	
		self.gattRequester.set_callback(callback)
		self.gattRequester.write_by_handle(0x28, '\x00\x00')
	
	
	def disconnect(self):
	
		if self.gattRequester != None and self.gattRequester.is_connected():
		
			time.sleep(1)
			self.gattRequester.disconnect()			
			self.gattRequester = None
			time.sleep(1)
