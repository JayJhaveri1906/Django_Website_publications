from django.db import models
from time import strftime
import datetime
from datetime import timezone,datetime
from django.core.exceptions import ValidationError

# Create your models her


class VRCPubs(models.Model):
    
    def present_or_past_date(value):
        
        x=datetime.today()
        value_date_=int(value.strftime("%Y")+value.strftime("%m")+value.strftime("%d"))
        date_=int(x.strftime("%Y")+x.strftime("%m")+x.strftime("%d")) 
        if value_date_>date_:
            raise ValidationError("The date cannot be in the future!")
        else:
            return value
       
            

        """value_year_=int(value.strftime("%Y"))
        value_month_=int(value.strftime("%m"))
        print(value.strftime("%m"))
        value_day_=int(value.strftime("%d"))
        print(value_year_, value_month_,value_day_)

        x=datetime.today()
        year_=int(x.strftime("%Y"))
        month_=int(x.strftime("%m"))
        day_=int(x.strftime("%d"))
        print(year_, month_,day_)

        if value_year_>year_:
            raise ValidationError("The date cannot be in the future!")
        elif value_year_<year_:
            return value
        else:
            if value_month_>month_:
                raise ValidationError("The date cannot be in the future!")
            elif value_month_<month_:
                return value
            else:
                if value_day_>day_:
                    raise ValidationError("The date cannot be in the future!")
                else:
                    return value"""
  

    title = models.CharField(max_length=1000)

    category = models.CharField(max_length=100)

    author= models.CharField(max_length=100)

    link= models.URLField()

    publishedAt=models.DateTimeField(validators=[present_or_past_date])

    isbn= models.CharField(max_length=100, blank=True)

    
    def __str__(self):
        return self.title

    def yearpublished(self):
        return self.publishedAt.strftime('%Y')

   

    

    
