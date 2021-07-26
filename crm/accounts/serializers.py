from rest_framework import serializers
from .models import *

class LaunchSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Launch
        
        fields = ['announced_date', 'status', 'name', 'brand','model','price']
    
class ResolutionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Resolution
        
        fields = ['height', 'width']  

class DimensionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Dimension
        
        fields = ['length','height', 'width']  

class BodySerializer(serializers.ModelSerializer):
    
    dimension = DimensionSerializer(many=False,read_only=True)
    
    class Meta:
        
        model = Body
        
        fields = ['weight_gram', 'build','sim_card','dimension']  


class DisplaySerializer(serializers.ModelSerializer):
    
    resolution = ResolutionSerializer(many=False,read_only=True)
    
    class Meta:
        
        model = Display
        
        fields = ['display_type', 'sizescreen','resolution']  


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Platform
        
        fields = ['operating_system', 'cpu','gpu','chipset']  

class MemorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Memory
        
        fields = ['card_slot', 'internal_memory']

class ConnectivitySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Connectivity
        
        fields = ['wlan', 'bluetooth','gps','nfc','infrared','radio','usb']

class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Camera
        
        fields = ['modules', 'features','video']

class BatterySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Battery
        
        fields = ['size', 'fast_charging']

class smartPhoneSerializer(serializers.ModelSerializer):
    
    launch        = LaunchSerializer(many=False,read_only=True)
    
    resolution    = ResolutionSerializer(many=False,read_only=True)
    
    dimension     = DimensionSerializer(many=False,read_only=True)
    
    body          = BodySerializer(many=False,read_only=True)
    
    display       = DisplaySerializer(many=False,read_only=True)
    
    platform      = PlatformSerializer(many=False,read_only=True)
    
    memory        = MemorySerializer(many=False,read_only=True)
    
    connectivity  = ConnectivitySerializer(many=False,read_only=True)
    
    main_camera   = CameraSerializer(many=False,read_only=True)

    selfie_camera = CameraSerializer(many=False,read_only=True)
    
    battery       = BatterySerializer(many=False,read_only=True) 
    
    class Meta:
        
        model = smartPhone
        
        fields = ['launch','resolution','dimension','body','display','platform','memory','connectivity','main_camera','selfie_camera','battery','picture']