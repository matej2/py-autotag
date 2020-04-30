from autotag.hashtags import get_hashtags
from autotag.settings import resources, image_dir


suggested_hashtags = get_hashtags(image_dir)


with open(resources + "/hashtags.txt", "w") as f:
    f.write(suggested_hashtags)
    f.close()
