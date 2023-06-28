from PIL import Image, ImageFilter

# Open an image file. The file path should be in the same directory as the notebook or a full path should be provided.
image = Image.open('example.jpg')

# Apply a filter to the image. In this case BLUR filter.
blurred_image = image.filter(ImageFilter.BLUR)

# Save the new image
blurred_image.save('blurred_example.jpg')

# Show the new image
blurred_image.show()

# Applying another filter, for example an edge enhancement filter.
edge_enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)

# Save the new image
edge_enhanced_image.save('edge_enhanced_example.jpg')

# Show the new image
edge_enhanced_image.show()

# Custom filters can also be applied
custom_filter = ImageFilter.Kernel((3, 3), [1, 1, 1, 0, 0, 0, -1, -1, -1], scale=1)
custom_filtered_image = image.filter(custom_filter)

# Save the custom filtered image
custom_filtered_image.save('custom_filtered_example.jpg')

# Show the custom filtered image
custom_filtered_image.show()
