from django.shortcuts import render
from .models import Organization, Parkingspot, Catparking, PublicUser, Getdata
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import json
from math import radians, cos, sin, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)

def availableseats(request):
    if request.method == 'POST':

        parks =  Parkingspot.objects.all()

        if 'gpsLong' not in request.POST and 'gpsLat' not in request.POST:
            return JsonResponse({'Error': "Please send gps longtitute and latitude [as gpsLong and gpsLat], optionally send maxDist, type of vehicle [as typeVeh], ramp and zoom."})
        
        responseData = {}

        for p in parks:

            if('typeVeh' not in request.POST):
                typeVeh = 'none'
            else:
                typeVeh = request.POST.get('typeVeh')

            if('ramp' not in request.POST):
                rampf = 0
            else:
                rampf = int(request.POST.get('ramp'))

            if('maxDist' not in request.POST):
                maxD = 10**6
            else:
                maxD = int(request.POST.get('maxDist'))
            catp = p.catid
            buildp = catp.orgid
            
            if((p.status=='free' or p.status=='unknown') and (typeVeh=='none' or typeVeh==catp.allowedvehicletype)):
                if(buildp.building):
                    dist = distance(p.spotlat, buildp.buildlat, p.spotlong, buildp.buildlong )
                    if(dist<maxD and rampf<=int(buildp.ramp)):
                        responseData[str(p.spotid)] = {'lat':p.spotlat, 'lng':p.spotlong, 
                        'building':1, 'ramp':int(buildp.ramp), 'dist':dist,
                        'type': catp.allowedvehicletype, 'status':p.status,'name':buildp.orgname}
                else:
                    responseData[str(p.spotid)] = {'lat':p.spotlat, 'lng':p.spotlong, 
                    'building':0, 'ramp':-1, 'dist':-1,
                    'type': catp.allowedvehicletype, 'status':p.status, 'name':buildp.orgname}

    response = JsonResponse(responseData)
    response = JsonResponse(responseData)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response

def saveseat(request):
    if request.method == 'POST':
        spot_id = request.POST.get('spot_id')
        gps_long = request.POST.get('gps_long')
        gps_lat = request.POST.get('gps_lat')

        try:
            sp = Parkingspot.objects.get(spotid=spot_id)
            print(gps_lat, sp.spotlat, gps_long, sp.spotlong)

            print(distance(float(gps_lat), float(sp.spotlat), float(gps_long), float(sp.spotlong)))
            if((sp.status == 'free' or sp.status == 'unknown') and distance(gps_lat, sp.spotlat, gps_long, sp.spotlong)<0.01):
                sp.status = 'occupied'
                sp.save()
                responseData = {
                    'id': spot_id,
                    'status': 'OK',
                }
            else:
                responseData = {
                    'id': spot_id,
                    'status': 'Taken',
                }

        except Exception as e:
            print(str(e))
            responseData = {
                'id': spot_id,
                'status': 'Wrong Coordinates',
            }
        response = JsonResponse(responseData)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response#JsonResponse(responseData)
    return render(request,'spots/hi.html')

def change(request, new_status):
    
    if request.method == 'POST':
        spot_id = request.POST.get('spot_id')

        try:
            sp = Parkingspot.objects.get(spotid=spot_id)

            if(sp.status == 'free' and new_status=='occ'):
                sp.status = 'occupied'
                sp.save()
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to occupied',
                }
            elif (sp.status == 'occupied' and new_status=="free"):
                sp.status = 'free'
                sp.save()                
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to free',
                }
            else:
                responseData = {
                    'id': spot_id,
                    'status': 'Not available',     
                }

        except:
            responseData = {
                'id': spot_id,
                'status': 'Wrong ID',
            }
        
        response = JsonResponse(responseData)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
    return render(request,'spots/hi.html')

def savedata(request):
    if request.method == 'POST':
        ans = json.loads(request.body)
        
        st = ans['data']
        #id = ans['applicationName'] κανονικα θα ειχαμε αυτο ομως επειδη στο testing 
        #εχουμε ενα αρντουινο και οχι ελεγχο πανω στo forwarding δεδομενων θα το ορισουμε 
        #ξεχωριστα από κατω κάνοντας force το id
        id = 1
        sentData = Getdata.objects.create(datatext =st)
        spot_id = id
        if st[0] == 'A':
            new_status = 'free'
        else:
            new_status = 'unknown' 
        try:
            sp = Parkingspot.objects.get(spotid=spot_id)
            if(sp.status == 'free' and new_status=='unknown'):
                sp.status = 'unknown'
                sp.save()
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to unknown',
                }
            elif (sp.status == 'occupied' and new_status=="free"):
                sp.status = 'free'
                sp.save()                
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to free',
                }
            elif (sp.status == 'unknown' and new_status=="free"):
                sp.status = 'free'
                sp.save()                
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to free from unknown',
                }
            else:
                responseData = {
                    'id': spot_id,
                    'status': "No changes detected",
                }

        except Exception as e:
            responseData = {
                'id': spot_id,
                'status': new_status,
                'error': str(e)
            }
        
    return JsonResponse(responseData)

def getTestMarkers(request):
    if request.method == 'POST':
        if 'gpsLong' not in request.POST and 'gpsLat' not in request.POST:
            return JsonResponse({'Error': "Please send gps longtitute and latitude [as gpsLong and gpsLat], optionally send maxDist, type of vehicle, ramp and zoom."})
        responseData = {'1':{'lat':38.268973, 'lng':21.748207, 'dist':30, 'type':'car', 'ramp':0}, '2':{'lat':38.268988, 'lng':21.748979, 'dist':35, 'type':'van', 'ramp':1}}
        return JsonResponse(responseData)
