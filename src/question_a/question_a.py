#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_miles_per_hour(KM,MIN):
    if KM < 0  or MIN < 0:
        return "invalid agruments" 
    else:      
        miles = KM * .621371
        hour = MIN/60
        MPH = miles/hour

        return MPH