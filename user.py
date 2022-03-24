# Mengchen Xu ID:61281584
# main module for user interface

import webapi
import mapclass

# function that convert list to string 
def list_to_str(result_list:list)->str:
    answer_str = ""
    for item in result_list:
        answer_str = answer_str + item + " "
    return answer_str

# function that generate all the user input into a list
def deal_input()->list:
    n = int(input())
    count_1 = 0
    answer_list = []
    answer_list.append(n)
    while count_1<n:
        content = input()
        answer_list.append(content)
        count_1+= 1
    m = int(input())
    count_2 = 0
    answer_list.append(m)
    while count_2<m:
        content = input()
        answer_list.append(content)
        count_2+= 1
    return answer_list

# function that get web result of infor dict
def build(start:str,end:str)->dict:
    url = webapi.build_search_url(start,end)
    result = webapi.get_result(url)
    return result

# function that print list nicely
def print_list(final_list:list):
    for item in final_list:
        print(item)
    print()

# function that print str nicely
def print_str(condition:str,final_list:list,units:str):
    answer = 0
    for item in final_list:
        answer += item
    print(condition + str(round(answer)) + units + "\n")

# function that deal with elevation
def deal_elevation(answer_list:list,index:int,i:int)->list:
    result = build(answer_list[i],answer_list[i+1])
    responce = webapi.combine_result(result,index)
#   create Elevation object
    a = mapclass.Elevation()
    r_list = a.action(responce)
    return r_list

# function that deal with latlong
def deal_Latlong(answer_list:list,index:int,i:int):
    result = build(answer_list[i],answer_list[i+1])
#   create Latlong object
    a = mapclass.Latlong()
    r_list = a.action(result,index)
    print(list_to_str(r_list))

# function that based on input to determine what to do 
def step(answer_list:list,m,n):
#   n is the number of the first line of input    
    r_list = []
    for j in range(m,m+n+2):
        if answer_list[j].upper()=="STEPS":
            final_list = []
            print("DIRECTIONS")
            for i in range(1,n):
                result = build(answer_list[i],answer_list[i+1])
#               create Step object
                a = mapclass.Steps()
                r_list = a.action(result)
                final_list.extend(r_list)
            print_list(final_list)
                    
        elif answer_list[j].upper()=="TOTALDISTANCE":
            final_list = []
            for i in range(1,n):
                result = build(answer_list[i],answer_list[i+1])
#               create TotalDis object
                a = mapclass.TotalDis()
                r_list = a.action(result)
                final_list.extend(r_list)
            print_str("TOTAL DISTANCE: ",final_list," miles")
                
        elif answer_list[j].upper()=="TOTALTIME":
            final_list = []
            for i in range(1,n):
                result = build(answer_list[i],answer_list[i+1])
#               create TotalTime object                
                a = mapclass.TotalTime()
                r_list = a.action(result)
                final_list.extend(r_list)
            print_str("TOTAL TIME: ",final_list," minutes")
                
        elif answer_list[j].upper()=="LATLONG":
            print("LATLONG")
            final_list = []
#          for-loop that get the latlongs of all the
#          different locations without the last location            
            for i in range(1,n):
                deal_Latlong(answer_list,0,i)
# statement to get the latlong of the final destination                
            deal_Latlong(answer_list,-1,i)
            print()
                    
        elif answer_list[j].upper()=="ELEVATION":
            print("ELEVATIONS")
            final_list = []
#          for-loop that get the elevations of all
#          different locations without the last location
            for i in range(1,n):
                r_list = deal_elevation(answer_list,0,i)
                final_list.extend(r_list)
# statements to get the elevation of the final destination
            r_list = deal_elevation(answer_list,-1,i)
            final_list.extend(r_list)
            print_list(final_list)
        else:
            print("Invalid output type: " + answer_list[j])

def handle():
    answer_list = deal_input()
    n = answer_list[0]
    m = answer_list[int(n)+1]
    print()
    for i in range(1,n):
        url = webapi.build_search_url(answer_list[i],answer_list[i+1])
        result = webapi.get_result(url)
    try:
        if result['info']['statuscode'] == 0:
            step(answer_list,m,n)
        elif result['info']['statuscode'] == 402:
            raise mapclass.NoRouteError
        else:
            raise mapclass.MapQuestError 
    except mapclass.MapQuestError:
        print("MAPQUEST ERROR")
    except mapclass.NoRouteError:
        print("NO ROUTE FOUND")
    finally:
        print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
  
if __name__ == '__main__':
    handle()

