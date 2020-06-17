from django.shortcuts import render, get_object_or_404
from .models import VRCPubs
from django.contrib import admin


# Create your views here.

def index(request):

    lst=[]
    years=[]
    CMPN_object=VRCPubs.objects.order_by('category','-publishedAt')
    for CMPN in CMPN_object:
        print(CMPN)
        if str(CMPN.category).upper() not in lst:
            lst.append(str(CMPN.category).upper())
        print(lst)

        if CMPN.yearpublished() not in years:
            years.append(CMPN.yearpublished())
        
        print(years)
    years=sorted(years, reverse=True)
    lst=sorted(lst)
    print(years)
    print(CMPN_object)
    return render(request,"CMPN/index.html", {'CMPN': CMPN_object, 'Categories':lst, 'years':years})

def year_detail(request,year_id):
    lst_objects=[]
    lst_category=[]
    year_objects=VRCPubs.objects.all()
    print("called year_detail")
    print(year_id)
    for year_object in year_objects:
        if int(year_object.yearpublished())==year_id:
            if str(year_object.category).upper() not in lst_category:
                lst_category.append(str(year_object.category).upper())
                print(year_id)
            lst_objects.append(year_object)
    lst_category=sorted(lst_category)
    print(lst_category)

    return render(request, 'CMPN/year_detail.html', {'id':year_id, 'req_objects':lst_objects , 'Categories':lst_category})