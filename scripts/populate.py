import os
import sys
import django
import uuid
import random
import string
from django.core.files import File

# Set up the Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cr8_api.settings')
django.setup()

from cr8_api.apps.prints.models import Print
from django.contrib.auth.models import User

def populate_db():
    covers_root = "store/covers/"
    stls_root = "store/stls/"

    c_files = os.listdir(covers_root)
    s_files = os.listdir(stls_root)

    # Get or create a default user
    default_user, _ = User.objects.get_or_create(username='default_user', defaults={'email': 'default@example.com'})

    for c, s in zip(c_files, s_files):
        generated_uuid = uuid.uuid4()
        dummy_str = ''.join(random.choices(string.ascii_letters, k=7))
        cover_path = os.path.join(covers_root, c)
        stl_path = os.path.join(stls_root, s)
        try:
            with open(cover_path, "rb") as cover_obj, open(stl_path, "rb") as stl_obj:
                cover = File(cover_obj)
                stl = File(stl_obj)

                # Create the Print object
                Print.objects.create(
                    id=generated_uuid,
                    creator=default_user,
                    title=dummy_str,
                    description=dummy_str,
                    cover=cover,
                    stl=stl,
                )
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Processing error")

if __name__ == "__main__":
    populate_db()