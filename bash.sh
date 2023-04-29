TIMESTAMP=$(date +"%s.%3N")
FILENAME="Image_$TIMESTAMP.jpg"
libcamera-jpeg -o $FILENAME
