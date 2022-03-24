# Mengchen Xu ID:61281584
# class module

# class of finding directions
class Steps:
    def action(self,result)->list:
        r_list = []
        for item in result['route']['legs']:
            for things in item['maneuvers']:
                r_list.append(things['narrative'])
        return r_list
# class of finding Total Distance
class TotalDis:
    def action(self,result)->list:
        r_list = []
        for item in result['route']['legs']:
            r_list.append(item['distance'])
        return r_list

# class of finding Total Time   
class TotalTime:
    def action(self,result)->list:
        r_list = []
        for item in result['route']['legs']:
            time = item['formattedTime']
            time_list = time.split(":")
            if time_list[0].startswith("0"):
                time_list[0] == time_list[0][-1]
            if time_list[-1].startswith("0"):
                time_list[-1] == time_list[-1][-1]
            if int(time_list[-1]) >= 30:
                minutes = int(time_list[0])*60 + int(time_list[1]) + 1
            else:
                minutes = int(time_list[0])*60 + int(time_list[1])
        r_list.append(minutes)
        return r_list

# class of finding latitude and longtitude           
class Latlong:
    def action(self,result,state)->list:
        r_list = []
        for item in result['route']['legs']:
            lati = item['maneuvers'][state]['startPoint']['lat']
            long = item['maneuvers'][state]['startPoint']['lng']
            if int(lati) >= 0:
                lati = str(round(lati,2)) + "N"
            else:
                a = round(lati,2)
                lati = str(a*-1) + "S"
            if int(long) >= 0:
                long = str(round(long,2)) + "E"
            else:
                o = round(long,2)
                long = str(o*-1) + "W"
        r_list.append(lati)
        r_list.append(long)
        return r_list

# class of finding elevation
class Elevation:
    def action(self,result)->list:
        r_list = []
        for items in result['elevationProfile']:
            elevation = round(items['height'] * 3.28084)
            r_list.append(elevation)
        return r_list

# class to create MapQuestError
class MapQuestError(Exception):
    pass

# class to create NoRouteError
class NoRouteError(Exception):
    pass


