[app]
# (str) Title of your application
title = AnimalApp

# (str) Package name
package.name = animalapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns = 

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Garden requirements
#garden_requirements = 

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = 

# (str) List of permissions to give to the app
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android entry point is a static library
#android.static_entry_point = False

# (str) Android bootstrap to use
#android.bootstrap = sdl2

# (str) Android service to use.
#android.service = 

# (bool) Android automatically provide permissions to install apps from unknown sources
#android.allow_storage = False