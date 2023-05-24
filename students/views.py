from django.shortcuts import render, redirect

# Create your views here.
from students.models import student
from students.form import PostForm

def listone(request):
    try:
        unit = student.objects.get(stdName="小名")
    except:
        errormessage = "讀取錯誤!"
    return render(request, "student/listone.html", locals())

def listall(request):
    allStudents = student.objects.all().order_by('id')
    return render(request, "student/listall.html", locals())

def post(request):
    if request.method == "POST":      #如果是以POST方式才處理
        stdName = request.POST['stdName'] #取得表單輸入資料
        stdID = request.POST['stdID']
        stdSex =  request.POST['stdSex']
        stdBirth =  request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone =  request.POST['stdPhone']
        stdAddress =  request.POST['stdAddress']
        #新增一筆記錄
        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress) 
        unit.save()  #寫入資料庫
        return redirect('/listall')  
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "student/addstudent1.html", locals())

def postform(request):
    #新增PostForm表單物件
    stdform = PostForm()
    if request.method == "POST":      #如果是以POST方式才處理
        stdName = request.POST['stdName'] #取得表單輸入資料
        stdID = request.POST['stdID']
        stdSex =  request.POST['stdSex']
        stdBirth =  request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone =  request.POST['stdPhone']
        stdAddress =  request.POST['stdAddress']
        #新增一筆記錄
        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress) 
        unit.save()  #寫入資料庫
        return redirect('/listall')  
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "student/stdform.html", locals())

def delete(request, stdID=None):
    if stdID != None:
        if request.method == "POST":
            stdID = request.POST["stdID"]
        try:
            unit = student.objects.get(stdID=stdID)
            unit.delete()
            return redirect('/listall')
        except:
            mess = "查無該學號"
    return render(request, "student/delete.html", locals())


def delete(request, stdID=None):
    if stdID != None:
        if request.method == "POST":
            stdID = request.POST["stdID"]
        # 嘗試抓取此id之學生資料
        # 嘗試try區塊的程式碼，如果發生錯誤或例外情形執行except區塊的程式碼
        try: 
            unit = student.objects.get(stdID=stdID)
            # 刪除該資料
            unit.delete()
            return redirect('/listall')
        except:
            mess = "查無該學號"
    return render(request, "student/delete.html", locals())

def edit(request, stdID=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(stdID=stdID)
        unit.stdName = request.GET["stdName"]
        unit.stdID = request.GET["stdID"]
        unit.stdSex = request.GET["stdSex"]
        unit.stdBirth = request.GET["stdBirth"]
        unit.stdEmail = request.GET["stdEmail"]
        unit.stdPhone = request.GET["stdPhone"]
        unit.stdAddress = request.GET["stdAddress"]
        unit.save()
        mess = "已修改完成"
        return redirect('/listall')
    else:
        try:
            unit = student.objects.get(stdID=stdID)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "此學號不存在"
        return render(request, "student/edit.html", locals())