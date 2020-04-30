import os
from pathlib import Path


# Directories
current_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
resources = os.path.join(Path(current_dir).parent, "target")

# Urls
page_url = "https://app.photerloo.com/InstagramHashtagKeywordingApp/"
image_dir = "/home/user/Downloads/test.jpg"


# Selectors
upload_input = "ngf-upload-photo-button"
hashtags = "#suggestedHashtags li"
