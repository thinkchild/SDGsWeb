from django.db import models

#Create your models here. 對應資料表
class BoardUnit(models.Model):
	bname = models.CharField(max_length=20, null=False)
	# bgender = models.BooleanField()
	bgender = models.CharField(max_length=2, default='F', null = False)
	btitle = models.CharField(max_length=100, null=False)
	bcontent = models.TextField(null=False)
	btime = models.DateTimeField(auto_now=True)
	bemail = models.EmailField(max_length=100, blank=True, default='')
	# 網站回覆內容
	bresponse = models.TextField(blank=True, default='')

	def _str_(self):
		return self.btitle