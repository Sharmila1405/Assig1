import requests
from bs4 import BeautifulSoup
import pandas




oyo_url = "https://www.oyorooms.com/hotels-in-banglore/?page="
page_num_MAX=3
scraped_info_list = []


for page_num in range(1, page_num_MAX):
   
    url = oyo_url + str(page_num)
    print("GET Requests for: "+url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div",{"class": "hotelCardLising"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3",{"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAdress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "llistingPrice__finalPrice"}).text

        try:
            hotel_dict["rating"] = hotel.find("span",{"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None

        parent_amenities_element = hotel.find("div",{"class":"amenityWrapper"})

        amenities_list =[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper--amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"] =','.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)
       

dataFrame = pandas.DataFrame(scraped_info_list)
print("Creating csv file...")
dataFrame.to_csv("Oyo.csv")