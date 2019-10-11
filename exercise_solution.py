# This is the solution to the small exercise in the tutorial notebook

# 1. Send an image through the network:

# The served model: MAX-Image-Caption-Generator
model_endpoint = 'http://max-image-caption-generator.max.us-south.containers.appdomain.cloud/' + 'model/predict'

# Upload an image to the MAX model's rest API
with open(my_image, 'rb') as file:
    file_form = {'image': (my_image, file, 'image/jpeg')} # note: set 'jpeg' to 'png' if working with a png image
    # Post the image to the rest API using the requests library
    r = requests.post(url=model_endpoint, files=file_form)
    # Return the JSON
    response = r.json()
    
# Show the output
print('----OUTPUT CAPTIONS----\n')
for i, x in enumerate(response['predictions']):
    print(str(i+1)+'.', x['caption'])

          
# 2. Extract the caption from the outpout
my_caption = response['predictions'][0]['caption']
print(my_caption)
