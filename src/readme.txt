Update DB:
----------
python manage.py schemamigration shop --auto
python manage.py migrate shop

Apps: sorl-thumbnail
--------------------
Required: ImageMagic (the simplest)
export IM_HOME=/Users/heikok/development/tools/ImageMagick-6.8.1
export DYLD_LIBRARY_PATH=$IM_HOME/lib/

