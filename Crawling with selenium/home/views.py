from django.shortcuts import render, redirect
from .forms import App_Search_forms, Google_Search_forms, Search_forms

from django.contrib import messages

from selenium import webdriver

# Create your views here.

def home(request):
	return render(request, 'home.html',{})

# for app/search page
def app_search(request):
	context = {"info":True}
	
	store_choice = request.GET.get('store_select', False)

	store_form = []
	if store_choice == '1':
		store_form = App_Search_forms(request.POST)
	else:
		store_form = Google_Search_forms(request.POST)

	context['store_select_form'] = Search_forms(request.GET or None)
	context['Store_form'] = store_form

	if request.POST:
		context['Store_form'].save()
		driver = webdriver.Chrome()
		if store_choice == '1':

			try:
				appname = context['Store_form'].cleaned_data.get('App_name')
				appid = context['Store_form'].cleaned_data.get('Application_id')
				package = "https://apps.apple.com/in/app/"+appname+"/id"+appid
				driver.get(package)
		
				app_icon = driver.find_elements_by_class_name("we-artwork__source")[0]
				app_icon = app_icon.get_attribute('srcset').split(" ")
				app_icon = app_icon[2]
				app_name = driver.find_element_by_class_name("app-header__title").text
				app_rating = driver.find_elements_by_class_name("we-customer-ratings__averages__display")[0].text
				total_ratings = driver.find_elements_by_class_name("we-customer-ratings__count")[0].text
				description_outer_div = driver.find_element_by_class_name("we-truncate--multi-line")
				description_p_tags = description_outer_div.find_elements_by_tag_name("p")
				description_full = ''
				for desc in description_p_tags:
					description_full += desc.text
				description = description_full[0:200] + '...' # truncate the description after first 200 characters 
			
			except:
				messages.info(request, f'An error occurs.Please enter correct App Name and Application_id!')
				return redirect('app-search')

			finally:
				driver.quit()

		else:

			try:
				package = context['Store_form'].cleaned_data.get('package_name')
				package = "https://play.google.com/store/apps/details?id="+package

				driver.get(package)
				main = driver.find_elements_by_class_name("xSyT2c")[0]
				image = main.find_elements_by_tag_name("img")
				app_icon=image[0].get_attribute('src')

				app_name = driver.find_elements_by_class_name("AHFaub")[0].find_elements_by_tag_name("span")[0].text
				description_full = driver.find_elements_by_class_name("DWPxHb")[0].text
				description = description_full[0:200] + '...'
				app_rating = driver.find_elements_by_class_name("BHMmbe")[0].text
				total_ratings = driver.find_elements_by_class_name("EymY4b")[0].text

			except:
				messages.info(request, f'An error occurs\nPlease enter correct Package Name!')
				return redirect('app-search')
			
			finally:
				driver.quit()

		context['info'] = {'Image':app_icon,'App_name':app_name, 'Description':description, 'Rating':app_rating, 'Total_ratings':total_ratings}
	return render(request, 'search.html',context)