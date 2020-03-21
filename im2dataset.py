from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Polar bears,baloons,Beaches","limit":100,"print_urls":True, "format":"jpg", "chromedriver":"C:\\Users\\Rajath\webdriver\\chromedriver"}

path = response.download(arguments)
print(path)