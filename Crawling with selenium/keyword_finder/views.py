from django.shortcuts import render, redirect
from .forms import url_form
from selenium import webdriver
from .models import info, URl

from django.contrib import messages

#store the data of URl models
data = URl.objects.all()
recommend = {}
# storing the data for checking recommendations
for ele in data:
	if ele.meta_data_container.name=="keywords":
		recommend[ele.site_url] = ele.meta_data_container.content.split(",")
 

# logic for recommendation 
def recommendation(comparison_list):
	count = 0
	recommend_urls = []
	for ele in comparison_list:
		for ele2 in recommend:
			count = recommend[ele2].count(ele)
			if count>=1:
				recommend_urls.append(ele2)

	return recommend_urls


# page keyword/finder
def find(request):
	# form a dictionary for data to print on page.
	context = {}
	context['form'] = url_form()
	context['meta_data']=[]
	context['recommend_urls'] = []
	if request.POST:
		context['is_fetching']=True
		# get the data input by user in site
		url = request.POST.get('site_url', False)
		# initializing driver.
		driver = webdriver.Chrome()
		try:
			driver.get(url)
			# extract data from site by tag name.
			meta_data = driver.find_elements_by_tag_name("meta")
			context['meta_data'] = []
			# Iterate over the meta_data.
			for ele in meta_data:
				name = ele.get_attribute("name")
				prop = ele.get_attribute("property")
				# check the data by its name and property.
				if name=="keywords" or name=="description" or prop=="og:description":
					content = ele.get_attribute("content")
					# check if proprty is given or not.
					if prop!=None:
						info_model=info(name=name, propert=prop, content=content)

					else:
						info_model=info(name=name, propert='', content=content)

					# save the info_model in database.
					info_model.save()
					# save the URl model in database.
					meta = URl(id=None, site_url=url, meta_data_container=info_model)
					meta.save() 
					# store the data to print on site in the dictionary context.
					context['meta_data'].append({'name':name,'property':prop ,'content':content})
					# store the recommended urls in the dictionary context.
					if name=="keywords":
						context['recommend_urls'].append(set(recommendation(content.split(","))))

		# redirect the user on same page with a message of error
		except:
			messages.info(request,f'Please enter correct url. You entered {url}!')
			return redirect('keyword-finder')
		# Finally quit the driver
		finally:
			driver.quit()
			context['is_fetching']=False


	return render(request, 'keyword.html', context)
