from django.shortcuts import render, redirect, get_object_or_404
from .forms import RideForm
from .models import MyBikeRides
# import requests module to connect to pink bike for web scraping
import requests
# import beautiful soup module and save as 'bs'
from bs4 import BeautifulSoup as bs


# API-trail search view
def mtb_trail_api(request):
    # if form method is POST, TRY/EXCEPT
    if request.method == 'POST':
        try:
            # get user input, in this case, a zip code, from the form
            trail_zip = request.POST.get('trail_zip')
            print(trail_zip)
            # API to change zip code to LAT/LON objects
            position_api = 'http://api.positionstack.com/v1/forward?access_key=50531561cf1dac34d4122f360cadf9b4&query=' + str(trail_zip)
            # connection object to positionstack API
            zip_conn = requests.get(position_api)
            # store JSON API response in the zip_data object
            zip_data = zip_conn.json()
            # get latitude and longitude by parsing through JSON returned data dictionary object
            lat = zip_data['data'][0]['latitude']
            lon = zip_data['data'][0]['longitude']
            # trail API using lat and lon objects to concat into the return URL
            trail_api_key = '200851898-d6ff4a881a3461e82c488db44a0eb8dc'
            trail_api = 'https://www.mtbproject.com/data/get-trails?lat=' + str(lat) + '&lon=' + str(lon) + '&maxDistance=50&maxResults=30&key=' + trail_api_key
            # connect to trail API
            trail_conn = requests.get(trail_api)
            # store return JSON data in the trail_data object
            trail_data = trail_conn.json()
            return render(request, 'MountainBikeApp/mtb_search_trails.html', {'trail_data': trail_data})
        except:
            error_msg = 'Zip Code Is Not Valid, Try Again!'
            return render(request, 'MountainBikeApp/mtb_search_trails.html', {'trail_data': None, 'error_msg': error_msg})
    return render(request, 'MountainBikeApp/mtb_search_trails.html', {'trail_data': None})



# beautiful soup mountain bike news page
def mtb_news_page(request):
    # website URL to connect, all Mountainbike world Press Releases on Gear and the sport
    # as a whole.
    mtb_url = 'https://www.pinkbike.com/news/press-releases/'
    # connection object using requests module
    news_page = requests.get(mtb_url)
    # content object using Beautiful Soup
    soup = bs(news_page.content, 'html.parser')
    # find container using ID in BS
    news_container = soup.find(id='news-container')
    # find all the news stories HTML stored in DIVs with class 'news-style1'
    news_stories = news_container.find_all('div', attrs={'class': 'news-style1'})
    # empty list to store dictionary objects in
    news_content = []
    # iterare through the divs as seen above and find titles, images and URL's to link
    # the story to my news page
    for story in news_stories:
        # empty dictionary object to append
        news = {}
        # title of the article
        news['title'] = story.find('a', class_='f22 fgrey4 bold').text
        # article image
        news['img'] = story.img['src']
        # url to specific article (image and title will be anchor tag)
        news['url'] = story.find('a', class_='f22 fgrey4 bold')['href']
        # type of media tag
        news['type_tag'] = story.find('a', class_='pb-tag news').text
        # date
        news['article_date'] = story.find('span', class_='fgrey2').text
        # add dictionary items in news and append them to the news_content list
        news_content.append(news)
    return render(request, 'MountainBikeApp/mtb_bs_news.html', {'news_content': news_content})

def mtb_about(request):
    return render(request, 'MountainBikeApp/mtb_about.html')

def mtb_home_page(request):
    return render(request, 'MountainBikeApp/mtb_home.html')

def mtb_index_page(request):
    rides = MyBikeRides.mtb_objects.all().order_by('-date_ridden')
    return render(request, 'MountainBikeApp/mtb_index.html', {'rides': rides})

# details page view start
def mtb_details(request, pk):
    pk = int(pk)
    ride_details = MyBikeRides.mtb_objects.get(id=pk)
    return render(request, 'MountainBikeApp/mtb_details.html', {'ride_details': ride_details})

# delete view page
def mtb_delete_confirm(request, pk):
    pk = int(pk)
    deleted_ride = MyBikeRides.mtb_objects.get(id=pk)
    ride_object_delete = deleted_ride.trail_network_name
    deleted_ride.delete()
    return render(request, 'MountainBikeApp/mtb_delete_confirm.html', {'ride_object_delete': ride_object_delete})

# update page view
def mtb_details_update(request, pk):
    mtb_instance = get_object_or_404(MyBikeRides, id=pk)
    mtb_form = RideForm(data=request.POST or None, instance=mtb_instance)
    if mtb_form.is_valid():
        mtb_form.save()
        return redirect('/MountainBikeApp/ride-index')
    return render(request, 'MountainBikeApp/mtb_update.html', {'mtb_form': mtb_form})

def mtb_create_ride(request):
    # call an instance of the form from forms.py
    form = RideForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rideindex')
    else:
        print(form.errors)
        form = RideForm()
    return render(request, 'MountainBikeApp/mtb_create_ride.html', {'form': form})
