from invoice.models import Invoice_FE, Wallet_FE
from pos.models import Invoice_POS, Wallet_POS
from company.models import Company, License
from employee.models import Employee
from client.models import Client
from data.models import Payment_Form
from inventory.models import Inventory
from settings.models import *
import json

class Create_Invoice:
	def __init__(self,data):
		self.data = data
		self.value = None
		if int(self.data[0]['type']) == 1:
			self.value = self.Create_Invoice_FE()
		else:
			self.value =  self.Create_Invoice_POS()

	def Discount_Inventory(self,quanty,code):
		inventory = Inventory.objects.get(code = code)
		inventory.quanty -= int(quanty)
		inventory.save()

	def Create_Invoice_FE(self):
		company = Company.objects.get(pk = self.data[0]['company'])
		consecutive = Consecutive_FE.objects.get(company = company)
		license = License.objects.get(company = company)
		if license.document_annual >= 1:
			for i in self.data:
				price = float(i['VAL. UNIT'])
				tax = i['IVA'].replace('%','')
				Invoice_FE(
					consecutive = consecutive.number,
					code = i['CODIGO'],
					description = i['DESCRIPCION'],
					price = price,
					tax = tax,
					discount = i['VAL. DESC.'],
					quanty = i['CANTIDAD'],
					date = self.data[0]['date'],
					date_expired = self.data[0]['date_expired'],
					time = self.data[0]['time'],
					payment_form = Payment_Form.objects.get(pk = self.data[0]['payment_form']),
					cancelled = self.data[0]['cancelled'],
					employee = Employee.objects.get(pk = self.data[0]['employee']),
					client = Client.objects.get(pk = self.data[0]['client']),
					company = company
				).save()
				self.Discount_Inventory(i['CANTIDAD'],i['CODIGO'])
			invoice = Invoice_FE.objects.filter(consecutive = consecutive.number)
			if not self.data[0]['cancelled']:
				Wallet_FE(
					invoice = invoice,
					company = invoice.company
				).save()
			total= 0

			for i in invoice:
				total += i.Total_Product()
			data = {
				'result':True,
				"pk": invoice.last().pk,
				"consecutive": consecutive.number,
				"client": invoice.last().client.name,
				"total": total,
				"state":invoice.last().state,
			}
			del invoice
			consecutive.number += 1
			consecutive.save()
			license.document_annual -= 1
			license.save()
		else:
			data = {'result':False}
		return data

	def Create_Invoice_POS(self):
		consecutive = Consecutive_POS.objects.last()
		company = Company.objects.get(pk = self.data[0]['company'])
		for i in self.data:
			price = float(i['VAL. UNIT'])
			tax = i['IVA'].replace('%','')
			Invoice_POS(
				consecutive = consecutive.number,
				code = i['CODIGO'],
				description = i['DESCRIPCION'],
				price = price,
				tax = tax,
				discount = i['VAL. DESC.'],
				quanty = i['CANTIDAD'],
				date = self.data[0]['date'],
				date_expired = self.data[0]['date_expired'],
				time = self.data[0]['time'],
				payment_form = Payment_Form.objects.get(pk = self.data[0]['payment_form']),
				cancelled = self.data[0]['cancelled'],
				employee = Employee.objects.get(pk = self.data[0]['employee']),
				client = Client.objects.get(pk = self.data[0]['client']),
				company = company,
			).save()
			self.Discount_Inventory(i['CANTIDAD'],i['CODIGO'])
		invoice = Invoice_POS.objects.filter(consecutive = consecutive.number)
		if not self.data[0]['cancelled']:
			Wallet_POS(
				invoice = invoice,
				company = invoice.company
			).save()
		total= 0
		for i in invoice:
			total += i.Total_Product()
		data = {
			"pk": invoice.last().pk,
			"consecutive": consecutive.number,
			"client": invoice.last().client.name,
			"total": total,
			'result':True
		}
		del invoice
		consecutive.number += 1
		consecutive.save()
		license = License.objects.get(company = company)
		license.document_annual -= 1
		license.save()
		return data

