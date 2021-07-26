from django.db import models
# Create your models here.
class Launch(models.Model):
    
    announced_date = models.DateField()
    
    status         = models.CharField(max_length=50) 
    
    name           = models.CharField(max_length=200) 
    
    brand          = models.CharField(max_length=200)
    
    model          = models.CharField(max_length=50) 
    
    price          = models.FloatField(max_length=50) 
    
    def __str__(self):
        return self.name

class Dimension(models.Model):      
       length   = models.FloatField()
    
       width   = models.FloatField()
    
       height  = models.FloatField()  
def __str__(self):
        return str(self.length)

class Body(models.Model):
    
    weight_gram    = models.IntegerField()
    
    build          = models.CharField(max_length=200) 
    
    sim_card       = models.CharField(max_length=200) 
    
    dimension      = models.ForeignKey(Dimension,on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.build +" "+str(self.weight_gram)
 


class Resolution(models.Model):
    
    height         = models.IntegerField()
    
    width          = models.IntegerField()
    
    def __str__(self):
        return str(self.height) +" "+str(self.width)



class Display(models.Model):
    
    display_type   = models.CharField(max_length=200) 
    
    sizescreen     = models.FloatField()
    
    resolution     = models.ForeignKey(Resolution,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.display_type 

class Platform(models.Model):
    
    operating_system = models.CharField(max_length=200) 
    
    chipset          = models.CharField(max_length=200) 
    
    cpu              = models.CharField(max_length=200) 
    
    gpu              = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.operating_system 

class Memory(models.Model):
    card_slot        =  models.CharField(max_length=200) 
    
    internal_memory  =  models.CharField(max_length=200) 
def __str__(self):
        return self.card_slot 


class Connectivity(models.Model):
    
    wlan       = models.CharField(max_length=50)
    
    bluetooth  = models.CharField(max_length=50)
    
    gps        = models.CharField(max_length=50)
    
    nfc        = models.CharField(max_length=50)
    
    infrared   = models.CharField(max_length=50)
    
    radio      = models.CharField(max_length=50)
    
    usb        = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.wlan 

class Camera(models.Model):
    
    modules  =  models.CharField(max_length=50)
    
    features =  models.CharField(max_length=50)
    
    video    =  models.CharField(max_length=50)          
   
def __str__(self):
        return self.modules 


class Battery(models.Model):
    
    size          =  models.IntegerField()
    
    fast_charging =  models.BooleanField()
    
    def __str__(self):
        
        return str(self.size)      


class smartPhone(models.Model):
     
     launch        = models.ForeignKey(Launch,on_delete=models.CASCADE,default="")
     
     body          = models.ForeignKey(Body,on_delete=models.CASCADE,default="") 
     
     display       = models.ForeignKey(Display,on_delete=models.CASCADE,default="") 
     
     platform      = models.ForeignKey(Platform,on_delete=models.CASCADE,default="") 
     
     memory        = models.ForeignKey(Memory,on_delete=models.CASCADE,default="") 
     
     main_camera   = models.ForeignKey(Camera,on_delete=models.CASCADE,related_name='main_cameratocamera',default="") 
     
     selfie_camera = models.ForeignKey(Camera,on_delete=models.CASCADE,related_name='selfie_cameratocamera',default="")  
     
     connectivity  = models.ForeignKey(Connectivity,on_delete=models.CASCADE,default="")  
     
     battery       = models.ForeignKey(Battery,on_delete=models.CASCADE,default="")
     
     picture       = models.ImageField(upload_to='pics',default="")  
    

        
