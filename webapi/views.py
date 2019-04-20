from rest_framework import views
from rest_framework.response import Response

from django.db import connections

from datetime import datetime

from django.utils.timezone import now


from django.http import HttpResponse


class SearchResultView(views.APIView):

	def post(self, request):
		starttime = request.POST["starttime"]
		stoptime = request.POST["stoptime"]
		servicetype = request.POST["servicetype"]
		servicetype = int(servicetype)
		return Response({"data":self.getresult(starttime,stoptime,servicetype)})

	def getresult(this,starttime,stoptime,servicetype):
		result = []
		if servicetype == 1:
			result = [{'id':5,'name':'คอมพิวเตอร์ P5','location':'ชั้น 1 อาคารเทพรัตน์วิทยาโชติ'},{'id':8,'name':'คอมพิวเตอร์ P6','location':'ชั้น 1 อาคารเทพรัตน์วิทยาโชติ'}]
		elif servicetype == 2:
			result = [{'id':5,'name':'ศึกษาเดี่ยว A5','location':'ชั้น 3 อาคารเทพรัตน์วิทยาโชติ'},{'id':8,'name':'ศึกษาเดี่ยว A7','location':'ชั้น 3 อาคารเทพรัตน์วิทยาโชติ'}]
		elif servicetype == 3:
			result = [{'id':5,'name':'ศึกษาเดี่ยว B8','location':'ชั้น 3 อาคารเทพรัตน์วิทยาโชติ'},{'id':8,'name':'ศึกษาเดี่ยว C2','location':'ชั้น 3 อาคารช่วงศิลปาการ'}]
		return result
